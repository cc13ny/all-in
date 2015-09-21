def longestChain(words):
    tb, lenlist = {}, []
    for word in words:
        if len(word) in tb:
            tb[len(word)][word] = -1
        else:
            tb[len(word)] = {word : -1}
            lenlist.append(len(word))
    lenlist.sort()

    dist, maxpossible = 1, len(lenlist)
    for i in range(len(lenlist) - 1, 0, -1):
        l = lenlist[i]
        if l - 1 == lenlist[i - 1]:
            for word in tb[l]:
                if tb[l][word] < 0:
            
            
        
    
