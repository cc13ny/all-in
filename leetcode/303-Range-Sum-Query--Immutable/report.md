Given an integer array _nums_, find the sum of the elements between indices i and j (i ¡Ü j), inclusive.

__Example:__

```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

__Note:__

1. You may assume that the array does not change.

2. There are many calls to sumRange function.

__Explanation:___

Here is one technique used often in 1-dim dp problems, i.e. ___Cumulative Sum___ or ___CS___. For example, we do _CS_ on [1, 2, 3], then we get [1, 3, 6].

Obviously, sumRang(i, j) = _cnums_[j] - _cnums_[i - 1] where _cnums_ is the array after _Cumulative Sum_-ing with the setting that _cnums_[-1] = 0.

__Code:__

```
class NumArray(object):
      def __init__(self, nums):
          csums = [0] + nums
          for i in range(len(nums)):
             csums[i + 1] += csums[i]
             self.csums = csums

      def sumRange(self, i, j):
          csums = self.csums
          assert -1 < i < len(csums) and -1 < j < len(csums)
	  return csums[j + 1] - csums[i]
```

__Question:__

Does "the array doesn't change" mean that it can't be modified?

If it can't be modified, is it suitable to use another array which is the modified version?
