'''
  Based on http://www.cnblogs.com/grandyang/p/4484571.html
'''


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0] * numCourses
        graphs = [set() for _ in
                  range(numCourses)]  # can't use [set()] * (numCourses). Otherwise, they influence each other
        for p in prerequisites:
            if p[0] not in graphs[p[1]]:  # handling corner case
                graphs[p[1]].add(p[0])
                indegrees[p[0]] += 1
        queue = [i for i in range(len(indegrees)) if indegrees[i] == 0]

        while len(queue) != 0:
            root = queue.pop(0)
            for i in graphs[root]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)

        if sum(indegrees) != 0:
            return False
        return True
