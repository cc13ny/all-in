def longestChain(words):
    lendict = {}
    lenlist = []

    # build the dictory where
    # the key is the length of a word,
    # and the value is the set of words with the length
    for word in words:
        l = len(word)
        if len(word) in lendict:
            lendict[l][word] = -1
        else:
            lendict[l] = {word : -1}
            lenlist.append(l)
    lenlist.sort()
    if len(lenlist) == 1:
        return 1
    
    maxsize = 1
    maxpossible = len(lenlist)
    for i in range(len(lenlist) - 1, 0, -1):
        l = lenlist[i]
        group = lendict[l]
        for word in group:
            lendict = lc(l, word, lendict)
            tmpsize = lendict[l][word]
            if tmpsize > maxsize:
                maxsize = tmpsize
                #if maxsize == maxpossible:
                #    return maxsize
        #maxpossible -= 1
        #if maxsize >= maxpossible:
        #    break
    print lendict
    return maxsize

def lc(l, word, lendict):
    if l not in lendict:
        return lendict
    if word not in lendict[l]:
        return lendict
    if lendict[l][word] != -1:
        return lendict
    
    if l - 1 not in lendict:
        lendict[l][word] = 1
        return lendict
    
    maxsize = 1
    for i in range(len(word)):
        nextword = word[:i] + word[i + 1:]
        lendict = lc(l - 1, nextword, lendict)
        if l - 1 in lendict and nextword in lendict[l - 1]:
            tmpsize = lendict[l - 1][nextword] + 1
            if tmpsize > maxsize:
                maxsize = tmpsize
    lendict[l][word] = maxsize
    print lendict
    return lendict
    
words = ['a', 'abcd', 'bcd', 'abd', 'cd', 'c']
words = ['a', 'aa', 'ba', 'aaa', 'aab', 'aac', 'aad', 'kkkk']
#words = ['bcd', 'abcd', 'a', 'aa', 'aaa', 'bbb']
#words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']

print longestChain(words)
