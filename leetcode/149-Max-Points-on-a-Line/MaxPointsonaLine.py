# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        pts = points
        lines = {}
        mto_cnt = {}
        for i in xrange(len(pts)):
            for j in xrange(i + 1, len(pts)):
                y1, y2, x1, x2 = pts[i].y, pts[j].y, pts[i].x, pts[j].x
                if y1 == y2 and x1 == x2:
                    mto_cnt[(x1, y1)] = mto_cnt.get((x1, y1), 0) + 1
                    continue
                dy, dx = float(y1 - y2), float(x1 - x2)
                idx = (dx / dx, -dy / dx, (x1 * dy - y1 * dx) / dx) if dx else (
                dx / dy, -dy / dy, (x1 * dy - y1 * dx) / dy)
                if idx not in lines:
                    lines[idx] = set()
                lines[idx].add((x1, y1))
                lines[idx].add((x2, y2))
        if not pts:
            return 0
        elif not lines:
            return len(pts)
        res = 0
        from math import sqrt
        for k in lines:
            tmp = len(lines[k])
            for p in mto_cnt:
                tmp += int(sqrt(2 * mto_cnt[p])) if p in lines[k] else 0
            res = max(res, tmp)
        return res
