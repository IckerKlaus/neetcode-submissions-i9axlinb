class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                lenght = 0
                while (num + lenght) in numSet:
                    lenght += 1
                longest = max(longest, lenght)
        return longest