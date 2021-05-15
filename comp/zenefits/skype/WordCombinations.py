# not optimized yet, should be optimized by dp

def combine(word, k):
    if k < 1 or k > len(word):
        return []
    if k == 1:
        return [word[i] for i in range(len(word))]
    res = combine(word[:-1], k)
    tmp = combine(word[:-1], k - 1)
    for t in tmp:
        res.append(t + word[-1])
    return res


res = combine('love', 2)
print
res
for r in res:
    print
    r
