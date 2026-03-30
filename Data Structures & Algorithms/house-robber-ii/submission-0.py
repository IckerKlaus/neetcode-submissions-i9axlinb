class Solution:
    def rob(self, nums: List[int]) -> int:      
        def robI(nums):
            # rob1, rob2, n, n+1, ...
            rob1, rob2 = 0, 0
            for n in nums:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        return max(nums[0], robI(nums[:-1]), robI(nums[1:]))