def maxprofit(stockvalues): 
    maxval, res = 0, 0
    for i in range(len(stockvalues) - 1, -1, -1):
        if maxval < stockvalues[i]:
            maxval = stockvalues[i]
        else:
            res += maxval - stockvalues[i]
    return res

stockvalues = [1, 3, 1, 2, 4]
print "Profit was: " + str(maxprofit(stockvalues))
