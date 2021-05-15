def mincost(vals):
    vals.sort()
    pairs = []  # (price, quantity), from max price to min

    pre, cnt = -1, 0
    for i in range(len(vals) - 1, -1, -1):
        if vals[i] != pre:
            if i != len(vals) - 1:
                pairs.append((pre, cnt))
            cnt = 1
            pre = vals[i]
        else:
            cnt += 1
    pairs.append((pre, cnt))

    row = {pairs[0][1]: pairs[0][0] * pairs[0][1]}  # freecnt : basecost
    # print pairs
    for i in range(1, len(pairs) - 1):
        # print row
        newrow = {}
        # preprice = pairs[i - 1][0]
        nowprice = pairs[i][0]
        nowcnt = pairs[i][1]
        for freecnt in row:
            basecost = row[freecnt]
            for free in range(min(freecnt, nowcnt) + 1):
                newfreecnt = freecnt + nowcnt - 2 * free
                newbasecost = basecost + nowprice * (nowcnt - free)
                if newfreecnt not in newrow or newrow[newfreecnt] > newbasecost:
                    newrow[newfreecnt] = newbasecost
        row = newrow

    cost = sum(vals)
    nowprice = pairs[-1][0]
    nowcnt = pairs[-1][1]
    # print
    for freecnt in row:
        basecost = row[freecnt]
        addcost = nowprice * (nowcnt - min(freecnt, nowcnt))
        # print freecnt, basecost
        # print basecost + addcost
        if basecost + addcost < cost:
            cost = basecost + addcost
    # print
    return cost


# mincost([3, 5, 6, 3, 2, 2, 2, 3])
tests = []
tests.append([100, 99, 2, 2])
tests.append([100, 99, 97, 97])
tests.append([100, 99, 97, 97, 96])
tests.append([100, 30, 30, 20, 10, 10, 10])

for vals in tests:
    print
    "prices are: " + str(vals)
    print
    "mincost is: " + str(mincost(vals))
    print
