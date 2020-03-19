class Solution:
    def max_network_rank(self, A, B, N):
        n = len(A)
        res = 0
        connected_counts = [0] * N
        for i in range(n):
            connected_counts[A[i]-1] += 1
            connected_counts[B[i]-1] += 1

        for i in range(n):
            res = max(res, connected_counts[A[i]-1] + connected_counts[B[i]-1] - 1)
        return res