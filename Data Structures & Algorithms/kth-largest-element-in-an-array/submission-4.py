class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time: O(n + k*logn)
        Space: O(n)
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]
