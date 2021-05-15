# Think about another ways

def mincoin(coins, target):
    # coins: positive nums
    coins.sort()
    cand = set(coins)
    minnums = [0] * target
    cnt = 0

    while len(cand) != 0:
        cnt += 1
        newcand = set()
        for c in cand:
            minnums[c] = cnt
            for coin in coins:
                idx = c + coin
                if idx < target:
                    print
                    2
                    if minnums[idx] == 0:
                        newcand.add(idx)
                else:
                    break
        cand = newcand
    return cnt


print
mincoin([1, 2], 3)
