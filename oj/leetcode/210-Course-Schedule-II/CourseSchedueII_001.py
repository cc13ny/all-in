# Based on the solution of CouseScheduleI
# However, I need to figure out my own solution


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees = [0] * numCourses
        graphs = [ set() for _ in range(numCourses) ]
        for p in prerequisites:
            if p[0] not in graphs[p[1]]:
                graphs[p[1]].add(p[0])
                indegrees[p[0]] += 1
        queue = [ i for i in range(len(indegrees)) if indegrees[i] == 0 ]
        res = queue[:]
        
        while len(queue) != 0:
            root = queue.pop(0)
            for i in graphs[root]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
                    res.append(i)
                
        if sum(indegrees) != 0:
            return []
        return res
