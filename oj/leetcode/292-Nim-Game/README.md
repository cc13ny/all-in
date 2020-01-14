001
---

It's my first version which used the ___rotation array___ introduced in the "rate limiter" section of Nine Chapter.

```py

def canWinNim(n):
    dp = [False] * 4
    cur = 0
    for i in range(n):
        dp[-1] = (not dp[0]) or (not dp[1]) or (not dp[2])
        dp[cur] = dp[-1]
        cur = (cur + 1) % 3
    return dp[-1]
```

It should work because the same soltuon in the almost same problem ["Coins in a Line"] (http://www.lintcode.com/en/problem/coins-in-a-line/) has passed.

The solution here is Memory Excess or TLE after _range(n)_ is changed as _xrange(n)_.

002
---

Based on the hint that __"If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?"__, I found the pattern [_Win, Win, Win, Lose, Win_, ...] which shows me the solution.
