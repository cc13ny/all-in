def maxdiff(nums):
    size = len(nums)
    minnum = [0] * size
    zeronum = [0] * size
    zeronum[0] = 1 if nums[0] == 0 else -1
    minnum[0] = 0 if nums[0] == 0 else -1
    for i in range(1, size):
        if nums[i] == 0:
            zeronum[i] = zeronum[i - 1] + 1
        else:
            zeronum[i] = zeronum[i - 1] - 1
        if minnum[i - 1] > zeronum[i]:
            minnum[i] = zeronum[i]
        else:
            minnum[i] = minnum[i - 1]
    print
    'minnum : ' + str(minnum)
    print
    'zeronum: ' + str(zeronum)
    for i in range(size):
        zeronum[i] -= minnum[i]

    mxdiff = max(zeronum)
    j = zeronum.index(mxdiff)
    i = -1 if minnum[j] == 0 else minnum.index(minnum[j])  # very small bug
    print
    print
    'Maximal diff at diff locations: ' + str(zeronum)
    print
    'max difference: ' + str(mxdiff)
    print
    'Number of 1s after flip-flop : ' + str(sum(nums) + mxdiff)
    if i != j:
        print
        print
        '(start, end) = (' + str(i + 1) + ', ' + str(j) + ')'
    else:
        print
        print
        'No Flip-Flop'
    print
    '-' * 50
    print
    'Before flip-flop : ' + str(nums)
    for idx in range(i + 1, j + 1):
        nums[idx] = 1 if nums[idx] == 0 else 0
    print
    'After  flip-flop : ' + str(nums)


test = []
test += [[1, 1, 1, 0, 0, 1, 1, 1]]
test += [[1, 1, 1, 1, 1, 1, 1, 1]]
test += [[0, 0, 1, 1, 1, 1, 1, 1]]
test += [[1, 0, 0, 1, 0, 0, 0, 1]]
for t in test:
    maxdiff(t)
    print
    '#' * 60
