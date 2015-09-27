# Think about how to improved based on this basis


def mincoin(coins, target):
    coins.sort()
    cnt = target
    for coin in coins:
        if target - coin >= 0:
            tmp = 1 + mincoin(coins, target - coin)
            if cnt > tmp:
                cnt = tmp
        else:
            break
    return cnt
            
print mincoin([1, 2], 3)
