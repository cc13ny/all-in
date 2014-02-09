Problem Description: Number of Ones
===================================
Given a postive natural number N in decimal form, you should count the number of 1's which appears within all numbere from 1 to N
  
E.g.
    N = 2, we have {1, 2}, only {1}, with 1 (1's);
    N = 12, we have {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, only {1, 10, 11, 12}, with 5 (1's);
    
Problem:
    1. Write a function f(x) which return the number of 1's from 1 to N, e.g. f(12) = 5
    2. Within the numbers with 32 digits at most, find out the biggest N such that f(N) = N
