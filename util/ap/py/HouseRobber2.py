'''
    You can run it directly to see results.
'''


def rob2(nums):
    # This problem is similar to Rober_I.
    #
    # However, for N houses,
    #   the 1st house and the Nth house
    #   can be robbed at the same time.
    #
    # So the tricky point is that this
    # problem can be divided into two
    # cases:
    #   1) The first house considered
    #      and the last one not included
    #
    #   2) The last house considered
    #      and the first house not included
    #
    # Note: 'considered' != 'included'
    #
    # More: there may be duplicate sub-cases
    #       between them, which can be
    #       optimal.

    if len(nums) == 1:
        return nums

    res1 = [0, 0] + nums[:-1]
    res2 = [0, 0] + nums[1:]

    for i in range(2, len(res1)):
        res1[i] = max(res1[i] + res1[i - 2], res1[i - 1])

    for i in range(2, len(res2)):
        res2[i] = max(res2[i] + res2[i - 2], res2[i - 1])

    end = len(res2) - 1

    return res2[1:] if res2[end] > res1[end] else res1[2:]


def find_path(nums, res):
    idx = []
    end = len(res) - 1
    i = end
    while i > - 1:
        if i > 0:
            if res[i] != res[i - 1]:
                idx = [i] + idx
                i -= 2
            else:
                i -= 1
        else:
            if end not in idx:
                # decide the first one or the last one
                # should not be included
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
    tests.append([1, 0, 1])

    return tests


def print_info(tests):
    n = 55
    print
    '#' * n
    print
    print
    'Problem: Robber II'
    print
    print
    '=' * n

    for i, t in enumerate(tests):
        assert t != []
        res = rob2(t)
        path = find_path(t, res)
        val_robb = [t[idx] for idx in path]

        print
        print
        'test case #' + str(i) + ':'
        print
        '     Maximal value: ' + str(res[len(res) - 1])
        print
        '     Values of each house: ' + str(t)
        print
        '     Indices of the path: ' + str(path)
        print
        '     Robbed values: ' + str(val_robb)
        print
        print
        '=' * n


def main():
    print_info(testcase())


if __name__ == "__main__":
    main()
