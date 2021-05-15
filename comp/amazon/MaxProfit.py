def maxprofit(stockvals):
    maxval, profit = 0, 0
    for stockval in stockvals[::-1]:
        maxval = max(maxval, stockval)
        profit += maxval - stockval
    return profit


stockvalues = [1, 3, 1, 2, 4]
print
"Profit was: " + str(maxprofit(stockvalues))
