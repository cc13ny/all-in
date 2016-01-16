For each bulb (e.g. the i_th bulb), it will be __on__ at the end if the total number of its factors (e.g. i) is __odd__.

001
---

So I tried the naive method at the beginning where I used an array to record the number of factors for each bulb, and got the total number of odd integers in the array.

```py
def bulbSwitch(n):
    res = 0
    num_of_facs = [1 for i in range(n)]
    for j in range(2, n + 1):
        for k in range(1, n / j + 1):
            num_of_facs[j * k - 1] += 1
            
    for num in num_of_facs:
        res += num % 2

    return res
```

002
---

It can be short with just one loop. Of course, it doesn't make big changes. Still TLE.

```py
def bulbSwitch(n):
    res = 0
    num_of_facs = [1 for i in range(n)]
    for j in range(2, n + 1):
        for k in range(1, n / j + 1):
            num_of_facs[j * k - 1] += 1
        res += num_of_facs[j - 1] % 2
    return res
```

003
---

Then, I figured out the 3rd solution which seems to be more complex. But the __basic idea__ is,

___The  number of factors of an integer is the product of all (the power of its prime factor plus one)___. 


Here is a [link] (http://www.cut-the-knot.org/blue/NumberOfFactors.shtml) for this conclusion. Take _12_ as an example, 12 = (2^__2__) * (3^__1__). So its number of factors is (__2__ + 1) * (__1__ + 1) = 6. Hence, if the power of one of its prime factor is odd, its number of factors must be even.

So I need an array to keep track of the primes before the integer for each bulb, and check the number of factors of an integer is odd or not.

```py
def bulbSwitch(n):
    res = 1
    primes = []
    for j in range(2, n + 1):
        m = j / 2
        case = 0
        for p in primes:
            cnt = 0
            if p > m:
               break
            elif j % p == 0:
                case = 1
                while t % p == 0:
                    t /= p
                    cnt += 1
                if cnt % 2 == 1:
                    case = 2
                    break
        if case == 0:
            primes.append(j)
        if case == 1:
            res += 1
    return res
```

Still TLE.

004
---

Using prime numbers in __003__ inspires me from the solution of the problem, [Count Primes] (https://leetcode.com/problems/count-primes/) as follows.

```py
def countPrimes(n):
    if n < 2:
        return 0
    booln = [True] * (n - 1)
    booln[0] = False
        
    for i in range(2, int(sqrt(n)) + 1): # Key Point 1
        if booln[i - 1]:
            for j in range(i * i, n, i): # Key Point 2
                booln[j - 1] = False
        
    res = 0
    for b in booln:
        if b:
            res += 1
    return res
```

Pay attention on the two __Key Points__ on the comments!

The __basic idea__ is, for any _c_ = _a_ * _b_ where 1 < _a_ , _b_, _c_ <= n, we shouldn't count _a_ * _b_ and _b_ * _a_ as two situations. 

Hence, we should set _a_ <= _b_. Then, _a_ * _a_ <= _a_ * _b_ = c <= n, i.e. _a_ <= sqrt(n) for the __1st Key Point__. For a fixed _a_, the allowed _b_ can be _a_, _a + 1_, ..., floor(n / a) for the __2nd Key Point__. So these two __Key Points__ counts each pair (_a_, _b_) such that _a_ <= _b_.



By using this method of counting, I figure out another solution for [Bulb Switcher] (https://leetcode.com/problems/bulb-switcher/).

```py
def bulbSwitch(n):
    res = 1
    num_of_facs = [2 for i in range(n)]
    for i in range(2, int(sqrt(n)) + 1): # Key Point 1
        for j in range(i * i, n, i): # Key Point 2
            num_of_facs[j - 1] += 2
        num_of_facs[i * i - 1] -= 1
        res += num_of_facs[j - 1] % 2
    
    for j in range(int(sqrt(n)) + 1, n):
        res += num_of_facs[j - 1] % 2
    return res
```

Memory Limit when for example, n = 9999999, then range(9999999) is too big. Then I __found__ from the last codes that 

1. num_of_facs[j - 1] += 2
2. num_of_facs[i * i - 1] -= 1

Only in the case 2, the number of factors is odd when j = i * i.

```py
def bulbSwitch(n):
    # res = 1
    # num_of_facs = [2 for i in range(n)]
    # for i in range(2, int(sqrt(n)) + 1): # Key Point 1
        # for j in range(i * i, n, i): # Key Point 2
        #    num_of_facs[j - 1] += 2
        # num_of_facs[i * i - 1] -= 1
        # res += num_of_facs[j - 1] % 2
    
    # for j in range(int(sqrt(n)) + 1, n):
    #    res += num_of_facs[j - 1] % 2
    return int(sqrt(n))
```

