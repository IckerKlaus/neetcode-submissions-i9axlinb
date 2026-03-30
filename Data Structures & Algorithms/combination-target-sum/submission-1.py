class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time: O(2^(target/min(nums)))
        Space: O(target/min(nums))
        """
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # including the index
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # not including the index
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res