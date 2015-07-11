'''
    You can run it directly to see results.
'''

def maxProfit(prices):
    # The idea is pretty simple.
    # for example: [1, 3, 2, 1]
    #   The maximal difference must appear in one of cases.
    #
    #   1. max([3, 2, 1]) - min([1])
    #   2. max([2, 1]) - min([1, 3])
    #   3. max([1]) - min([1, 3, 2])
    if len(prices) < 2:
        return 0

    minn = prices[:-1]
    maxn = prices[1:]

    mi = minn[0]
    for i in range(1, len(minn)):
        if minn[i] > mi:
            minn[i] = mi
        else:
            mi = minn[i]
            
    ma = maxn[-1] # the last element
    for i in range(len(maxn) - 1, 0, -1):
        if maxn[i] > ma:
            ma = maxn[i]
        else:
            maxn[i] = ma

    res = 0
    for i in range(len(maxn)):
        if maxn[i] - minn[i] > res:
            res = maxn[i] - minn[i]

    return res

def find_path(res, prices):
    # It can be optimized, however,
    # I just leave it to be not too complext
    if len(prices) < 2:
        return []

    mi = prices[0]
    for i in range(len(prices) - 1):
        if i == 0:
            for j in range(1, len(prices)):
                if mi + res == prices[j]:
                    return [i, j]
        elif mi > prices[i]:
            mi = prices[i]
            for j in range(i+1, len(prices)):
                if mi + res == prices[j]:
                    return [i, j]
    return []        
        

def testcase():
    # test case
    tests = []
    tests.append([1, 3, 2, 1])
    tests.append([1])
    tests.append([])
    tests.append([4, 3, 2, 1])
    # for non-increasing case, nothing to buy and sell

    return tests

def print_info(tests):
    n = 60
    print '#' * n
    print
    print 'Problem: Best Time to Buy and Sell Stock I'
    print
    print '=' * n

    for j, t in enumerate(tests):
        prices = t
        maxprofit = maxProfit(prices)

        print
        print 'test case #' + str(j) + ':'
        print '     prices             : ' + str(prices)
        print '     max_profit         : ' + str(maxprofit)
        print '     buy and sell days  : ' + str(find_path(maxprofit, prices))
        print
        print '=' * n

def main():
    print_info(testcase())

if __name__ == "__main__":
    main()
