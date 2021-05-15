def longest_chain(w):
    lendict, lenlist = {}, []
    for word in w:
        l = len(word)
        if l in lendict:
            lendict[l].add(word)
        else:
            lendict[l] = set([word])
            lenlist.append(l)
    lenlist.sort()

    if len(lenlist) < 2:
        return len(lenlist)

    maxsize = 1

    for i in range(len(lenlist) - 1, 0, -1):
        l = lenlist[i]
        group = lendict[l].copy()
        for word in group:
            tmpsize, lendict = lc(l, word, lendict)
            if tmpsize > maxsize:
                maxsize = tmpsize
    return maxsize


def lc(l, word, lendict):
    if (l not in lendict) or (word not in lendict[l]):
        return 0, lendict
    lendict[l].remove(word)
    if l - 1 not in lendict:
        return 1, lendict
    maxsize = 1
    for i in range(len(word)):
        nextword = word[:i] + word[i + 1:]
        res, lendict = lc(l - 1, nextword, lendict)
        tmpsize = res + 1
        if tmpsize > maxsize:
            maxsize = tmpsize
    return maxsize, lendict


words = ['a', 'abcd', 'bcd', 'abd', 'cd', 'c']
words = ['a', 'aa', 'ba', 'aaa', 'aab', 'aac', 'aad', 'kkkk']
words = ['bcd', 'abcd', 'a', 'aa', 'aaa', 'bbb']
words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']

print
longest_chain(words)
