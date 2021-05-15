def sym_x_exist(points):
    l, r = min(points), max(points)
    mid_x = (l[0] + r[0]) / 2.0
    pts = set(points)
    for p in points:
        if (2 * mid_x - p[0], p[1]) not in pts:
            return False
    return True


tests = []
tests.append([(1, 2), (-1, 2), (3, 4), (-3, 4)])
tests.append([(1, 2), (-1, 2), (3, 4), (3, 5)])

for test in tests:
    print
    sym_x_exist(test)
