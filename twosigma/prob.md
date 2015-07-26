Q1. Given 1 GB (N) memory, you're asked to sort 1TB (M) data

A1: 1TB = 1024GB. We sort each batch of size 1GB.  So there're 1024 batches of sorted data.

    Base: [1024 * 2^(30) log (2^ 30)] = 2^40 * 30 log 2
    
    Plus: 
        1) (1024 log 1024) + (2^40 - 2^10) log (2^10) = 2^40 log 2^10
        
        2) (2^30 log 2^30) + (2^40 - 2^30) log (2^30) = 2^40 log 2^30
    
    So I will choose the first one.
    
My question is, why not make the "Plus" as 2log2. However, the prerequisite is that I need to make sure the first n (e.g. 2, 1024, 2^30) must be the first n of all numbers. For example, each head number of each sorted array forms the first 1024 numbers. This question is similar to 赛马问题。
