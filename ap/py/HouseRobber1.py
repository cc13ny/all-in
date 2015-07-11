'''
    You can run it directly to see results.
'''

def rob(nums):
    # Output (res):
    #   For i > 1, res[i] stors the maximal value
    #   you can rob from the first (i - 1) houses.
    #  	For example, res[2] is the maximal value
    #   you can get from the 1st house (the only
    #   one)
    #
    #   The first two values of res are just
    #  	compatible with the calculation of
    #   res[2] and res[3]. However, there's no
    #   meaning for them.     
    res = [0, 0] + nums 
    for i in range(2, len(res)):
        res[i] = max(res[i] + res[i-2], res[i-1])
        # same: res[i] = max(nums[i-2] + res[i-2], res[i-1])
    return res[2:]

def find_path(nums, res):
    #Note: the 'res' here is same as 'res[2:]' in 'rob' function
    idx = []
    i = len(res) - 1
    while i > - 1:
        if i > 0:
            if res[i] != res[i-1]:
                # which means if res[i] = res[i-1] because the ith house is not robbed
                idx = [i] + idx
                i -= 2
            else:
                i -= 1
        else:
            idx = [0] + idx
            i -= 1
    return idx

def testcase():
    # test cases
    # assume that each value is an non-negative integer and there's one house at least.
    tests = []
    tests.append([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    tests.append([1, 2])
    tests.append([1])

    return tests

def print_info(tests):

    n = 55
    print '#' * n
    print
    print 'Problem: Robber I'
    print
    print '=' * n

    for i, t in enumerate(tests):
        assert t!=[]
        res = rob(t)
        path = find_path(t, res) 
        val_robb = [t[idx] for idx in path]

        print
        print 'test case #' + str(i) + ':'
        print '     Maximal value: ' + str(res[len(res) - 1])
        print '     Values of each house: ' + str(t)
        print '     Indices of the path: ' + str(path)
        print '     Robbed values: ' + str(val_robb)
        print
        print '=' * n

def main():
    print_info(testcase())

if __name__ == "__main__":
    main()
