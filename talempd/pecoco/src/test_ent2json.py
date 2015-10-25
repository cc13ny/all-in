"""
This module is used to run unittests for each classes & methods of entry2json.py which has been tested on Ubuntu 14.04 and Window 8.
"""

import entry2json as ej
import unittest
from collections import OrderedDict

# report/ result can be written into log, but not implemented here
class MyTest(unittest.TestCase):
    '''
    MyTest is a class inherited from unittest.TestCase for testing all methods of entry2json.py .
    '''
    def test_validColor(self):
        '''
        Test validColor function (in Validation class) which always returns True now.
        '''
        testcases = [('Red', True), ('Black', True), ('Blue', True)]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(vld.validColor(test), truth)
        print 'Passed: method \'validColor\' in class \'Validation\''
        
    def test_validName(self):
        '''
        Test validName function (in Validation class) on 3 different cases: ('', False), ('He2e', False), ('Jack', True).
        1. ('', False) represents the case where the normalized name is '' .
        2. ('He2e', False) represents the case where a name contains digits .
        3. ('Jack', True) represents the normal case beyond cases mentioned above.
        '''
        testcases = [('', False), ('He2e', False), ('Jack', True)]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(vld.validName(test), truth)
        print 'Passed: method \'validName\' in class \'Validation\''
        
    def test_validPhoneNum(self):
        testcases = [('888-888-8888', True), ('5432', False), ('555555-1111111', False)]
        '''
        Test validPhoneName function (in Validation class) on 3 different cases: ('888-888-8888', True), ('5432', False), ('555555-1111111', False).
        1. ('888-888-8888', True) represents the normal case where the string contains exactly 10 digits.
        2. ('5432', False) represents the case where the string contains less than 10 digits.
        3. ('555555-1111111', False) represents the case where the string contains more than 10 digits.
        '''
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(vld.validPhoneNum(test), truth)
        print 'Passed: method \'validPhoneNum\' in class \'Validation\''
        
    def test_validZipCode(self):
        '''
        Test validZipCode function (in Validation class) on 4 different cases: ('12345', True), ('5432667', False), ('12a34', False).
        1. ('12345', True) represents the normal case where the string contains exactly 5 consecutive digits.
        2. ('5432667', False) represents the case where the string contains more than 5 characters.
        3. ('5432', False) represents the case where the string contains less than 5 characters.
        4. ('12a34', False) represents the case where the 5 characters contain non-digits.
        '''
        testcases = [('12345', True), ('5432667', False), ('5432', False), ('12a34', False)]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(vld.validZipCode(test), truth)
        print 'Passed: method \'validZipCode\' in class \'Validation\''

    def test_normColor(self):
        '''
        Test normColor function (in Normalizer class) where it should the string without spaces at the two ends.
        '''
        
        testcases = [('Red', 'Red'), (' Black ',  'Black'), ('Blue        ', 'Blue')]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(nlz.normColor(test), truth)
        print 'Passed: method \'normColor\' in class \'Normalizer\''

    def test_normName(self):
        '''
        Test normName function (in Normalizer class) where it should the string without spaces at the two ends.
        '''
        testcases = [('  Jack ', 'Jack'), (' Sam ',  'Sam')]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(nlz.normName(test), truth)
        print 'Passed: method \'normName\' in class \'Normalizer\''

    def test_normPhoneNum(self):
        '''
        Test normPhoneName function (in Normalizer class) on 3 different cases: ('  111-1151-1111111 ', ''), (' 542 ',  ''), ('(888)-888-8888', '888-888-8888').
        1. (('  111-1151-1111111 ', '') represents the case where the string contains more than 10 digits.
        2. (' 542 ',  '') represents the case where the string contains less than 10 digits.
        3. ('888-888-8888', True) represents the normal case where the string contains exactly 10 digits.
        '''
        testcases = [('  111-1151-1111111 ', ''), (' 542 ',  ''), ('(888)-888-8888', '888-888-8888')]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(nlz.normPhoneNum(test), truth)
        print 'Passed: method \'normPhoneNum\' in class \'Normalizer\''
        
    def test_normZipCode(self):
        '''
        Test normZipCode function (in Normalizer class) where it should the string without spaces at the two ends.
        '''
        testcases = [('  15 12 3 ', '15123'), ('',  ''), (' 15213 ', '15213')]
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(nlz.normZipCode(test), truth)
        print 'Passed: method \'normZipCode\' in class \'Normalizer\''
        
    def test_process(self):
        '''
        Test process function (in Converter class) on 7 different cases from 2 groups: valid & invalid.
        
        Invalid:
            1. ('a1231', None) represents the case where the number of elements splitted by ',' is less than 4.
            2. ('Booker T., Washington, 87360, 373 781 7380, yellow, RUBBISH', None) represents the case where the number of elements splitted by ',' is more than 5.
            3. ('Booker T., Washington, 87360, 373 781, yellow', None) represents the case where the number of elements splitted by ',' is 5, however, it doesn't match any format.
            4. 'James Murphy, yellow, 83880, 018 154 64', None) represents the case where the number of elements splitted by ',' is 4, however, it doesn't match any format.

        Valid:
            3 normal cases represent 3 different formats respectively.
        '''
        testcases = []

        # Check the number of element is valid
        testcases.append(('a1231', None))
        testcases.append(('Booker T., Washington, 87360, 373 781 7380, yellow, RUBBISH', None))

        # If it doesn't match one of 3 formats
        testcases.append(('Booker T., Washington, 87360, 373 781, yellow', None))
        testcases.append(('James Murphy, yellow, 83880, 018 154 64', None))

        # Normal cases
        mp = OrderedDict()
        nl_ord_ent = ['red', 'Ben', 'Chen', '937-321-8951', '11220']
        for i in range(len(nl_ord_ent)):
            mp[ele_names[i]] = nl_ord_ent[i]
        testcases.append(('Chen, Ben, (937)-321-8951, red, 11220', mp))

        mp = OrderedDict()
        nl_ord_ent = ['yellow', 'Booker T.', 'Washington', '373-781-7380', '87360']
        for i in range(len(nl_ord_ent)):
            mp[ele_names[i]] = nl_ord_ent[i]
        testcases.append(('Booker T., Washington, 87360, 373 781 7380, yellow', mp))

        
        mp = OrderedDict()
        nl_ord_ent = ['yellow', 'James', 'Murphy', '018-154-6474', '83880']
        for i in range(len(nl_ord_ent)):
            mp[ele_names[i]] = nl_ord_ent[i]
        testcases.append(('James Murphy, yellow, 83880, 018 154 6474', mp))
        
        for testcase in testcases:
            test, truth = testcase
            self.assertEqual(cvt.process(test), truth)
        print 'Passed: method \'process\' in class \'Converter\''
        
    def test_ent2json(self):
        '''
        Test process function (in Converter class) on 5 different cases.
        1. ('test/small.in', 'test/small.truth') represents a small input file which includes valid entries & erros.
        2. ('test/only_errors.in', 'test/only_errors.truth') represents an input file which only includes erros.
        3. ('test/only_entries.in', 'test/only_entries.truth') represents an input file which pnly includes valid entries.
        4. ('test/nothing.in', 'test/nothing.truth') represents an input file which includes nothing.
        5. ('test/large.in', 'test/large.truth') represents a large input file which includes valid entries & erros.
        '''
        testcases = []
        testcases.append(('test/small.in', 'test/small.truth'))
        testcases.append(('test/only_errors.in', 'test/only_errors.truth'))
        testcases.append(('test/only_entries.in', 'test/only_entries.truth'))
        testcases.append(('test/nothing.in', 'test/nothing.truth'))
        testcases.append(('test/large.in', 'test/large.truth'))
        for testcase in testcases:
            inputfile, truthfile = testcase

            cvt.ent2json(inputfile)
            with open (inputfile[:-2] + 'out', 'r') as f:
                output = f.read()
            
            with open (truthfile, 'r') as f:
                truth = f.read().strip()
            self.assertEqual(output, truth)
        print 'Passed: method \'ent2json\' in class \'Converter\''

if __name__ == "__main__":
    ele_names = ej.ele_names
    fac = ej.Factory()
    vld, nlz, cvt = fac.vld, fac.nlz, fac.cvt
    unittest.main()
