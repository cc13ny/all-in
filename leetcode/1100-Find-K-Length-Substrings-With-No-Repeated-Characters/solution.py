class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        count = 0
        idx_hash = {}
        start_idx, end_idx = 0, 0

        n = len(S)
        while start_idx <= (n - K) and end_idx < n:
            char = S[end_idx]
            if char in idx_hash and end_idx > idx_hash[char] >= start_idx:
                start_idx = idx_hash[char] + 1

            idx_hash[char] = end_idx

            if end_idx - start_idx + 1 == K:
                count += 1
                start_idx += 1
            else:
                end_idx += 1
        return count