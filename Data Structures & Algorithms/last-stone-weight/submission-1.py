class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time: O(nlogn)
        Space: O(n)
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y > x: heapq.heappush(stones, x - y)
        stones.append(0)
        return abs(stones[0])