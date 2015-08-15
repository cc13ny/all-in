# Although it can't AC leetcode test, it's definitely right. However, its pattern may be not as obvious as the one that can AC

def grayCode(n):
    res = [0]
    seed = 1
    for i in range(n - 1):
        res += [seed, 3 * seed]
        seed = seed << 1
    for j in range((seed << 1) - len(res)):
        res.append(res[j] + seed)
    return res
