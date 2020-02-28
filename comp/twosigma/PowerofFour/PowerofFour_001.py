def isPowerOfFour(n):
    return n > 0 and n & n - 1 is 0 and n & 0x5555555555555555 != 0
