class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(index): #starting in 0
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[ndex]
            subset.append(nums[index])
            dfs(index + 1)

            # NOT include nums[index]
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res