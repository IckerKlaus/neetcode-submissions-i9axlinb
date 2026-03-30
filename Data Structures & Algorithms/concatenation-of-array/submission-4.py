class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums) * 2
        while len(ans) < size:
            for num in nums:
                ans.append(num)
        return ans