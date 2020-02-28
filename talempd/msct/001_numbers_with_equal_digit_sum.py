class Solution:
    def digit_sum(self, num):
        # positive and negative numbers
        num = abs(num)
        tot = 0
        for l in str(num):
            tot += ord(l) - 48
        return tot

    def num_with_equal_digit_sum(self, A):
        res = -1
        ds_to_top_2 = {}
        for num in A:
            ds = self.digit_sum(num)
            if ds in ds_to_top_2:
                arr = ds_to_top_2[ds]
                i = 0
                while i < len(arr):
                    if arr[i] <= num:
                        break
                    i += 1
                arr.insert(i, num)
                arr = arr[:2]
                res = max(res, sum(arr))
            else:
                ds_to_top_2[ds] = [num]
        return res