class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        count = 0
        idx_hash = {}
        first_idx, last_idx = 0, 0

        n = len(S)
        while first_idx <= (n - K) and last_idx < n:
            char = S[last_idx]
            if char in idx_hash:
                if idx_hash[char] != last_idx and idx_hash[char] >= first_idx:
                    first_idx = idx_hash[char] + 1

            idx_hash[char] = last_idx

            if last_idx - first_idx + 1 == K:
                count += 1
                first_idx += 1
            else:
                last_idx += 1
        return count