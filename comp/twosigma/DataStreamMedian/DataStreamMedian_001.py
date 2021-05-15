import heapq as hq


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def medianII(self, nums):
        # write your code here
        if len(nums) < 2:
            return nums
        minheap = []
        maxheap = []
        sandwich = [maxheap, nums[0], minheap]
        res = [nums[0]]
        for i in range(1, len(nums)):
            print
            sandwich
            mid = sandwich[1]
            num = nums[i]
            if len(maxheap) == len(minheap):
                if mid <= num:
                    hq.heappush(minheap, num)
                else:
                    if len(maxheap) == 0:
                        sandwich[1] = num
                    else:
                        top = -hq.heappop(maxheap)
                        if top < num:
                            sandwich[1] = num
                            hq.heappush(maxheap, -top)
                        else:
                            sandwich[1] = top
                            hq.heappush(maxheap, -num)
                    hq.heappush(minheap, mid)
            else:
                if mid <= num:
                    top = hq.heappop(minheap)
                    if top < num:
                        sandwich[1] = top
                        hq.heappush(minheap, num)
                    else:
                        sandwich[1] = num
                        hq.heappush(minheap, top)
                    hq.heappush(maxheap, -mid)
                    # maxheap.append(0)
                else:
                    hq.heappush(maxheap, -num)
                    # maxheap.append(0)
            res.append(sandwich[1])
        return res


s = Solution()
tests = []
tests.append(range(1, 6))
tests.append([4, 5, 1, 3, 2, 6, 0])
tests.append([2, 20, 100])
tests.append([2, 20, 13, 18, 15, 8, 3, 5, 4, 25])
tests.append([5, -10, 4])

for t in tests:
    print
    s.medianII(t)
