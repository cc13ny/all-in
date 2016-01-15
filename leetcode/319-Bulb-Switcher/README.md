For each bulb (e.g. the i_th bulb), it will be on at the end if the total number of its factors (e.g. i) is odd.

001
---

So I tried the naive method at the beginning where I used an array to record the number of factors for each bulb, and got the total number of odd numbers in the array.

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

___The  number of factors of an integer is the product of (the power of its prime factor plus one)___. 


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

Pay attention on the two key points on the comments!

Its time complexity is O(n) because the outer loop takes O(sqrt(n)) and the inner loop takes O(sqrt(n)). 

The outer loop
