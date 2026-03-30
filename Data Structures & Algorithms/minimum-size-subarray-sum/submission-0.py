class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        lenght = float('inf')
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                lenght = min(lenght, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if lenght == float('inf') else lenght