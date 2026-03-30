class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            minHeap.append([dist,[x, y]])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, coord = heapq.heappop(minHeap)
            res.append(coord)
            k -= 1
        return res
