001
---

Use list to record each available location (0-location)

```py
def moveZeroes(nums):
    zeropos = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeropos.append(i)
        elif zeropos != []:
            idx = zeropos.pop(0)
            nums[idx] = nums[i]
            nums[i] = 0
            zeropos.append(i)
```

002
---

Better than 001, O(1) space, shorter & concise code

```py
def moveZeroes(nums):
    j = -1
    for i in range(len(nums)):
        if j < 0 and nums[i] == 0:
            j = i
        if j >= 0 and nums[i] != 0:
            nums[j], nums[i] = nums[i], 0
            j += 1
```

003
---

The most concise, and perfect

```py
def moveZeroes(self, nums):
    j = 0
    for i in xrange(len(nums)):
        if nums[i]:
            nums[i], nums[j] = 0, nums[i]
            j += 1
```
