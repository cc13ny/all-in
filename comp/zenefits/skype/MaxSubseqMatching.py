def ismatched(word, p, k):
    pk = ''
    for c in p:
        pk += c * k
    
    i, j = 0, 0
    while i < len(pk) and j < len(word):
        if pk[i] == word[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i < len(pk):
        return False
        
    return True


def maxmatch(word, p):
    if len(word) < len(p):
        return 0

    maxnum = 0
    maxcnt = {}
    for c in p:
        maxcnt[c] = 0
        
    for c in word:
        if c in maxcnt:
            maxcnt[c] += 1
            if maxcnt[c] > maxnum:
                maxnum = maxcnt[c]
    maxnum = min(len(word) / len(p), maxnum)
    minnum = 0
    while minnum <= maxnum:
        midnum = minnum + (maxnum - minnum) / 2
        if ismatched(word, p, midnum):
            minnum = midnum + 1
        else:
            maxnum = midnum - 1
    return maxnum


tests = []
tests.append(('xxaxybyxyzxxxzzz', 'xyxz'))

for t in tests:
    print maxmatch(t[0], t[1])
