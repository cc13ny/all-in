The idea is same as [this one](https://leetcode.com/discuss/98173/o-log-n-time-solution-with-explanation) and [the answer in this one](https://leetcode.com/discuss/98276/why-factor-2-or-3-the-math-behind-this-problem). I just write it with my style in a concise way.


    1. class Solution(object):
    2.   def integerBreak(self, n):
    3.        if n < 4:
    4.            return n - 1
    5.
    6.        n3 = (n - 2) / 3
    7.        rem = (n - 2) % 3
    8.        return (3 ** n3) * (rem + 2)


The maths behind the solution are __re-described__ here:

#1. Have been mentioned [here](https://leetcode.com/discuss/98173/o-log-n-time-solution-with-explanation) 

Assume that ___n = m + (n - m)___ where ___m___ and ___(n - m)___ are positive numbers.

> __n__ should be broken into numbers of ___2___ and ___3___, i.e. __n = n2  * 2 + n3 * 3__.

##Proof
For positive integer ___m___, to break it into ___2___ and ___m - 2___ , __won't decrease__ the product of positive integers, the sum of which is ___n___ , if ___2(m - 2) >= m___ , i.e. ___m >= 4___ .However, the positive numbers less than 4 include ___1, 2, 3___. In other word, for ___n___,  __n = n1 * 1 + n2  * 2 + n3 * 3__.

+ For 1, to break ___m___ into ___1___ and ___(m - 1)___ is useless because it doesn't increase the product.
+ For 2, as described above.
+ For 3, to break it into ___3___ and ___m - 3___ , won't decrease the product , if ___3(m - 3) >= m___ , i.e. ___m >= 4.5___

----------------------------
>  __n2 <=2__ .

##Proof
For ___2 + 2 + 2___, we can make it as ___3 + 3___ where __3 * 3 > 2 * 2 * 2__.  Thus, ___n2 <= 2___.

#2. My Adaption

___n___ can be represented in one of following expressions:

+ n = n3 * 3 + 0 * 2
+ n = n3 * 3 + 1 * 2
+ n = n3 * 3 + 2 * 2

They can be re-arranged as follows.

+ n = n3' * 3  + 2
+ n = n3' * 3  + 3
+ n = n3' * 3  + 4

__[Note that 4 = 2 + 2 = 2 * 2]__

Hence, line 6 in my code is used to calculate __n3'__ and line 8 with __(rem + 2)__ is used for the remaining part of the product, especially it happens that __4 = 2 + 2 = 2 * 2__.
