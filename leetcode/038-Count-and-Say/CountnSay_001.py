class Solution:
    # @param {integer} n
    # @return {string}
    def built_from_prev(self, s):
        nums = [s[0]]
        counts = [1]
        for i in range(1, len(s)):
            if s[i] == nums[-1]:
                counts[-1] += 1
            else:
                nums.append(s[i])
                counts.append(1)
        res = ''
        for i in range(len(nums)):
            res += str(counts[i]) + nums[i]
        return res
            
    def countAndSay(self, n):
        s = '1'
        for i in range(1, n):
            s = self.built_from_prev(s)
        return s
