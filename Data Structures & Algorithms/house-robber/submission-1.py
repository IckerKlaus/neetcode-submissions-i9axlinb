class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Bottom up Dynamic Programming
        Time: O(n)
        Space: O(1)
        """
        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
