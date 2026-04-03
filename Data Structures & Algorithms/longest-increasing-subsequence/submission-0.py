class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIST = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]: LIST[i] = max(LIST[i], 1 + LIST[j])
        return max(LIST)