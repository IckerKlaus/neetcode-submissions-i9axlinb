class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm O(n) instead of nested loops O(n^2)
        maxSum = nums[0]
        curSum = 0
        
        for num in nums:
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)
        
        return maxSum