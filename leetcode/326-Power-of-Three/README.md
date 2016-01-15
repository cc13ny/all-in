It's a kind of tricky problem while it's also easy. 

At the begining, I tried to take advantage of bit operations and figure out any special characters for "Power of Three". However, at the end I can't figure out, and it seems that I entered into a dead end, although I maybe know that. Finally, I searched [an answer](http://bookshadow.com/weblog/2016/01/08/leetcode-power-three/) which just simply used the LOG operation that it still makes use of a loop inside, like by Newton method.

Another tricky point (which I still can't figure out) is, 

```py

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == 3 ** round(math.log(n, 3)) # not work, e.g. for 45
        return n > 0 and 3 ** round(math.log(n, 3)) == n

```
