"""
[2, 3, 6, 2, 4] stones

[0, 6, 4, 2, 2, 3] max heap stones

"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])