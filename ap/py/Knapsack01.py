'''
    You can run it directly to see results.
'''

def knapsack01(sizes, vals, S):
    #aux[i][s] is the maximal value given the first (i-1) items under the size limitation: s
    aux = [[-1 for _ in range(S + 1)] for _ in vals]
    for i in range(len(vals)):
        for s in range(S+1):
            if i == 0:
                aux[0][s] = 0 if sizes[0] > s else vals[0]
            else:
                # For the case of the first(i+1) items (i.e. aux[i][s]), there're 2 cases:
                #
                #                  Include the (i+1)th item or Not
                #
                # If the (i+1)th item is bigger than the size limitation, then we won't put
                # it in the bag. Then the case for the first i items is same for the first
                # (i+1) items. Otherwise, it will be compared with for the case of the first
                # i items after the (i+1)th item is included.

                res = 0 if s < sizes[i] else aux[i-1][s-sizes[i]] + vals[i]
                aux[i][s] = max(aux[i-1][s], res)
    return aux

def find_path(aux, sizes):
    S = len(aux[0]) - 1
    i = len(aux) - 1
    idx = []
    
    while i > 0: 
        if aux[i][S] > aux[i-1][S]:
            # Only if these two values are different, it means that
            # the (i+1)th item is included
            idx = [i] + idx
            S -= sizes[i]
        i -= 1
    
    if S >= sizes[0]:
        idx = [0] + idx
    return idx


def testcase():
    # test case
    tests = []
    tests.append(([1, 2, 3, 2, 2], [8, 4, 0, 5, 3], 5))
    tests.append(([1, 2, 3, 2, 2], [8, 4, 0, 5, 3], 6))
    tests.append(([1, 2, 3, 2, 2], [8, 4, 0, 5, 3], 7))
    tests.append(([1], [7], 8))

    return tests

def print_info(tests):
    n = 60
    print '#' * n
    print
    print 'Problem: KnapSack01'
    print
    print '=' * n

    for j, t in enumerate(tests):
        sizes = t[0]
        vals = t[1]
        S = t[2]
        
        aux = knapsack01(sizes, vals, S)
        idx = find_path(aux, sizes)
        sub_sizes = [sizes[i] for i in idx]
        sub_vals = [vals[i] for i in idx]
        print
        print 'test case #' + str(j) + ':'
        print '     sizes: ' + str(sizes)
        print '     vals : ' + str(vals)
        print '     S    : ' + str(S)
        print
        print '     Auxiliary Matrx :'
        for a in aux:
            print '             ' + str(a)
        print
        print '     Subset Indices : ' + str(idx)
        print '     Subset Sizes   : ' + str(sub_sizes)
        print '     Subset Vals    : ' + str(sub_vals)
        print
        print '     Subset Size Sum: ' + str(sum(sub_sizes))
        print '     Subset Val  Sum: ' + str(sum(sub_vals))
        print
        print '=' * n

def main():
    print_info(testcase())

if __name__ == "__main__":
    main()
