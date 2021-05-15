def conflicts(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: intervals[0])
    pairs = []
    for i in range(len(intervals) - 1):
        fstend = intervals[i][1]
        for j in range(i + 1, len(intervals)):
            sndstart = intervals[j][0]
            if sndstart < fstend:
                pairs.append((intervals[i], intervals[j]))
            else:
                break
    return pairs


test = [(1, 8), (2, 6), (3, 5), (9, 10)]

pairs = conflicts(test)

for pair in pairs:
    print
    pair
