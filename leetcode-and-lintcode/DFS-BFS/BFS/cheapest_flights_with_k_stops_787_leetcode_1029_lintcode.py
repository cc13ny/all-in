'''
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
https://www.lintcode.com/problem/1029/solution/19171
'''


'''
TLE, the last stop, i.e. desc has to be handled specifically.
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]

        to_desc = []

        for flight in flights:
            i, j, price = flight
            adj[i].append((j, price))
            if j == dst:
                to_desc.append((i, price))



        min_cost_from_src = [float('inf')] * n
        min_cost_from_src[src] = 0

        queue = [src]
        stops = 0
        level_cnt = 1

        while queue and stops <= k-1:
            i = queue.pop(0)
            level_cnt -= 1
            for j, price in adj[i]:
                min_cost_from_src[j] = min(price + min_cost_from_src[i], min_cost_from_src[j])
                queue.append(j)

            if level_cnt == 0:
                stops += 1
                level_cnt = len(queue)

        for i, price in to_desc:
            min_cost_from_src[dst] = min(price + min_cost_from_src[i], min_cost_from_src[dst])

        return min_cost_from_src[dst] if min_cost_from_src[dst] != float('inf') else -1




