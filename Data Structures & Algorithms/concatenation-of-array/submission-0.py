class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        ans[len(nums):] = nums
        return ans