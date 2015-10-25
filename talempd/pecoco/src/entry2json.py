"""
This module is used to parse entries of personal information and write them as the formatted & valid JSON into an output file. Please check details of requirments from 'rolodex_instructions.pdf' in the root directory of this project.
"""

import json
import re
from collections import OrderedDict

ele_names = ['color', 'firstname', 'lastname', 'phonenumber', 'zipcode']

class Factory():
    '''
    Factory is the class as the set of 3 classes for this task: Normalizer, Validation, Converter  
    '''
    def __init__(self):
        """
        Construct a new 'Factory' object
        
        :attr vld: Instance of Validation Object
        :attr nlz: Instance of Normalizer Object
        :attr cvt: Instance of Converter Object
        
        :return: nothing
        """
        self.vld = Validation()
        self.nlz = Normalizer(self.vld)
        self.cvt = Converter(self.vld, self.nlz)
        

class Normalizer():
    def __init__(self, validation):
        """
        Construct a new 'Normalizer' object
        
        :param validation: Instance of Validation Object
        
        :attr normfunc: a list of functions of Normalization for different elements of a valid entry
        :attr vld: Instance of Validation Object
        
        :return: nothing
        """
        
        normfunc = [self.normColor, self.normName, self.normName, self.normPhoneNum, self.normZipCode]
        self.normfunc = normfunc
        self.vld = validation
        
    def normColor(self, color):
        """
        Normalize color
        
        :param color: a string for color name
        
        :return: a string without spaces of two ends
        """
        return color.strip()

    def normName(self, name):
        """
        Normalize name
        
        :param name: a string for person's firstname or lastname
        
        :return: a string without spaces of two ends
        """
        return name.strip()
    
    def normPhoneNum(self, num):
        """
        Normalize phone number
        
        :param num: a string for phone number
        
        :return: a formatted string like '888-888-8888' if num is valid. Otherwise, ''.
        """
        num = num.strip()
        if self.vld.validPhoneNum(num):
            nl_num = ''.join(re.findall(r'\d+', num))
            nl_num = nl_num[:3] + '-' + nl_num[3:6] + '-' + nl_num[6:10]
            return nl_num
        return ''
        
    def normZipCode(self, code):
        """
        Normalize zip code
        
        :param code: a string for zip code
        
        :return: a string without spaces
        """
        return ''.join(code.split())
                         
    def normAll(self, ord_ent):
        """
        Normalize all elements of an entry
        
        :param ord_ents: a list of all ordered elements of an entry
        
        :return: a list of all normalized & ordered elements of an entry
        """
        nl_ord_ent = []
        
        nf = self.normfunc
        for i in range(len(ord_ent)):
            nl_ord_ent.append(nf[i](ord_ent[i]))
        
        return nl_ord_ent
    

class Validation():
    def __init__(self):
        """
        Construct a new 'Validation' object
            
        :attr valfunc: a list of functions of Validation for different elements of an entry

        :return: nothing
        """
        valfunc = [self.validColor, self.validName, self.validName, self.validPhoneNum, self.validZipCode]
        self.valfunc = valfunc
        
    def validColor(self, color):
        # We can create a set of color names.
        # If 'color' is not in the set, return False
        """
        Validate color
        
        :param color: a string for color name
        
        :return: True
        """
        
        return True

    def validName(self, name):
        # We maybe need the validation for first & last name separately
        # Maybe needed if required: return False if it contains any special char instead of '.'
        """
        Validate name
        
        :param name: a string for person's firstname or lastname
        
        :return: False if it contains nothing or any digits. Otherwise, True.
        """
        
        if name == '':
            return False
        if bool(re.search(r'\d', name)):
            return False

        return True
    
    def validPhoneNum(self, num):
        # Assumption
        """
        Validate phone number
        
        :param num: a string for phone number
        
        :return: False if it doesn't contain exactly 10 digits. Otherwise, True.
        """
        if len(''.join(re.findall(r'\d+', num))) == 10:
            return True
            
        return False
        
    def validZipCode(self, code):
        # Don't know any restriction for each number of zipcode.
        # But I can check details via https://en.wikipedia.org/wiki/ZIP_code#Structure_and_allocation
        """
        Validate zip code
        
        :param code: a string for zip code
        
        :return: False if it is not exactly 5 consecutive digits. Otherwise, True.
        """
        
        if len(code) != 5:
            return False
        
        if not code.isdigit():
            return False
            
        return True
                         
    def validAll(self, nl_ord_ents):
        """
        Validate all elements of an entry
        
        :param nl_ord_ents: a list of all normalized & ordered elements of an entry
        
        :return: False if any element is not valid. Otherwise, True
        """
        
        vf = self.valfunc
        for i in range(len(nl_ord_ents)):
            if not vf[i](nl_ord_ents[i]):
                return False
        
        return True

        
class Converter():
    def __init__(self, validation, normalizer):
        """
        Construct a new 'Converter' object

        :param validation: Instance of Validation Object
        :param normalizer: Instance of Normalizer Object
            
        :attr vld: Instance of Validation Object
        :attr nlz: Instance of Normalizer Object

        :return: nothing
        """
        
        self.vld = validation
        self.nlz = normalizer
        
    def process(self, line):
        """
        Process each row/ line/ entry of the input file. There're 6 steps for processing where some are missed if the line is invalid.

        1. Check the number of elements is valid. It's valid if the number is 4 or 5. Otherwise, return None.

        2. Decide which format it is (one of three formats). It's based on the idx of the phone number.

        3. Reorder elements based on the corresponding pattern.

        4. Normalize all elements of the orderd & valid entry.

        5. Check if the entry is valid.

        6. Contruct the mapping. The mapping is an ordered dict with the ordered keys ['color', 'firstname', 'lastname', 'phonenumber', 'zipcode'], and their corresponding elements from the entry
    
        :param line: a row/ line/ entry of the input file
        
        :return: None if the line is invalid. Otherwise, the mapping.
        """
        
        # Check the number of elements is valid
        ent = line.split(',')
        nelemnts = len(ele_names)
        if len(ent) != nelemnts and len(ent) != nelemnts - 1:
            return None
        
        # Decide which format it is (one of three formats)
        if len(ent) == nelemnts - 1:
            if len(ent[0].rsplit(None, 1)) != 2:
                return None
            [Firstname, Lastname] = ent[0].rsplit(None, 1)
            ent = [Firstname, Lastname] + ent[1:]
        
        phone_num_candidates = ent[2:5]
        ptype = -1
        for i in range(3):
            if self.vld.validPhoneNum(phone_num_candidates[i]):
                ptype = i
                break
        if ptype == -1:
            return None

        # Reorder elements based on the corresponding pattern
        ptrns = [[3, 1, 0, 2, 4], [4, 0, 1, 3, 2], [2, 0, 1, 4, 3]]
        ord_ent = [ent[idx] for idx in ptrns[ptype]]

        # Normalize all elements of the orderd & valid entry
        nl_ord_ent = self.nlz.normAll(ord_ent)

        # Check if the entry is valid
        if not self.vld.validAll(nl_ord_ent):
            return None

        # Contruct the mapping
        mp = OrderedDict()
        for i in range(len(nl_ord_ent)):
            mp[ele_names[i]] = nl_ord_ent[i]
    
        return mp

    def ent2json(self, fname):
        """
        Parse each line / entry of personal information from an input file, and write them as the formatted & valid JSON into an output file.

        :param fname: the absolute or relative path of input file

        :return: nothing
        """
        res = OrderedDict([('entries',[]), ('errors', [])])
        
        with open(fname) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                mapping = self.process(lines[i])
                if mapping is not None:
                    res['entries'].append(mapping)
                else:
                    res['errors'].append(i)
        
        if res['entries'] == []:
            del res['entries']
        else:
            entries = sorted(res['entries'], key = lambda t: (t['lastname'], t['firstname']))
            res['entries'] = entries
            
        if res['errors'] == []:
            del res['errors']

        with open(fname[:-2] + 'out', 'wb') as outfile:
            if res != OrderedDict():
                json.dump(res, outfile, indent=2)        

if __name__ == "__main__":
    fac = Factory()
    vld, nlz, cvt = fac.vld, fac.nlz, fac.cvt
    print 'Please input the absoulte path of the input file'
    fname = raw_input()
    cvt.ent2json(fname)
