class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        
        for i in range(max(len(nums) - k, 1)):
            if i == 0:
                tmp = nums[:k + 1]
                tmp.sort()
                for j in range(len(tmp) - 1):
                    if abs(tmp[j + 1] - tmp[j]) <= t:
                        return True
            else:
                l, r = 0, k
                while l <= r:
                    m = (l + r) / 2
                    if tmp[m] < nums[i - 1]:
                        l = m + 1
                    elif tmp[m] > nums[i - 1]:
                        r = m - 1
                    else:
                        break
                tmp.pop(m)
                
                l, r = 0, k - 1
                while l <= r:
                    m = (l + r) / 2
                    if abs(tmp[m] - nums[i + k]) <= t:
                        return True
                    if tmp[m] < nums[i + k]:
                        l = m + 1
                    else:
                        r = m - 1
                tmp.insert(l, nums[i + k])
        return False
