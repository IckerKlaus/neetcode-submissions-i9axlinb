class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            index[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i, index[diff]]
