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

It can be short with just one loop.

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
