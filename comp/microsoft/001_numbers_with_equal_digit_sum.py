class Solution:
    def digit_sum(self, num):
        # positive and negative numbers
        num = abs(num)
        tot = 0
        while num:
            tot += num % 10
            num //= 10
        return tot

    def num_with_equal_digit_sum(self, A):
        res = -1
        ds_to_top = {}
        for num in A:
            ds = self.digit_sum(num)
            if ds in ds_to_top:
                top = ds_to_top[ds]
                res = max(res, top + num)
                ds_to_top[ds] = max(top, num)
            else:
                ds_to_top[ds] = num
        return res
