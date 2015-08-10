def longestChain(words):
    if words == []:
        return 0
    lendict = {}
    lenlist = []

    # build the dictory where
    # the key is the length of a word,
    # and the value is the set of words with the length
    for word in words:
        l = len(word)
        if len(word) in lendict:
            lendict[l][word] = 1
        else:
            lendict[l] = {word : 1}
            lenlist.append(l)
    lenlist.sort()
    
    maxsize = 1
    for i in range(1, len(lenlist)):
        l = lenlist[i]
        if l - 1 in lendict:
            group = lendict[l]
            for word in group:
                for j in range(len(word)):
                    nextword = word[:j] + word[j + 1:]
                    if nextword in lendict[l - 1]:
                        tmpsize = lendict[l - 1][nextword] + 1
                        if tmpsize > lendict[l][word]:
                            lendict[l][word] = tmpsize
                            if tmpsize > maxsize:
                                maxsize = tmpsize
            
    return maxsize
    
words = ['a', 'abcd', 'bcd', 'abd', 'cd', 'c']
words = ['a', 'ab', 'abc', 'abcd', 'eeeeeeee', 'e']
print longestChain(words)
