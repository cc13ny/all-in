def max_subseq_sort(A):
    A.sort()
    l, m, res = 0, 0, 0
    for r in range(len(A)):
        if A[m] != A[r]:
            m = r
        if A[r] - A[l] > 1:
            l = m
        #print l, m, r
        res = max(res, r - l + 1)
    return res
        

def max_subseq_hash(A):
    cnts = {}
    for a in A:
        cnts[a] = cnts.get(a, 0) + 1

    res = 0
    for a in cnts:
        nx_cnt = cnts.get(a + 1, 0) 
        res = max(res, cnts[a] + nx_cnt)
    return res
