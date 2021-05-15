'''
    You can run it directly to see results.
'''


def lnis(nums):
    # res is a 0-based array where
    # res[i] stores the length

    # of lnis ending the number nums[i]
    #

    # So when we output the length of
    # lnis of the whole integer array,
    # we will print max(res) instead of
    # the last one of res.

    res = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] <= nums[j] and res[j] >= res[i]:
                res[i] = res[j] + 1
    return res


def find_path(res):
    idx = [0]
    cnt = 2
    flag = True

    # If res[i] stores the length of lnis
    # of the first (i+1) numbers instead of
    # the length of lnis ending the number nums[i]
    #
    # Then, res should look like:
    #           [1, 1, 1, 2, 2, 3, 3]
    # So the idx [2, 3, 5] is what we need, i.e.
    # the last 1, and every first other numbers
    # where the changes of lengh happen.
    #
    # However, we can use the original res. That is,
    # to find the last before any change, and the
    # locations where each change happens.

    for i in range(len(res)):
        if res[i] == 1 and flag:
            idx[0] = i
        elif res[i] == cnt:
            idx.append(i)
            cnt += 1
            flag = False
    return idx


def testcase():
    # test cases
    # assume that there's one element at least.
    tests = []
    tests.append([5, 6, 3, 6, 7, 2])

    n = 55
    print
    '#' * n
    print
    print
    'Problem: Longest Non-Increasing Sub-sequence'
    print
    print
    '=' * n

    for i, t in enumerate(tests):
        assert t != []
        res = lnis(t)
        path = find_path(res)
        subseq = [t[idx] for idx in path]

        print
        print
        'test case #' + str(i) + ':'
        print
        '     Longest Length: ' + str(max(res))
        print
        '     Array of Integers ' + str(t)
        print
        '     Indices of the path: ' + str(path)
        print
        '     Longest Non-increasing Subsequence: ' + str(subseq)
        print
        print
        '=' * n


def main():
    testcase()


if __name__ == "__main__":
    main()
