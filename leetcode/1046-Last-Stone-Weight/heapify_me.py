class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] = - stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            diff = y - x
            if diff:
                heapq.heappush(stones, diff)
        return -stones[0] if stones else 0