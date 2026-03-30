class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre_fix = 1
        for i in range(len(nums)):
            res[i] = pre_fix
            pre_fix *= nums[i]
        pos_fix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos_fix
            pos_fix *= nums[i]
        return res