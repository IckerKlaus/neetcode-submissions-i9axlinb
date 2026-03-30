class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = {}
        res = []
        for num in nums:
            if num not in freqNums:
                freqNums[num] = 1
            else:
                freqNums[num] += 1
        
        for _ in range(k):
            key_max = max(freqNums, key=freqNums.get)
            res.append(key_max)
            freqNums.pop(key_max) 
        
        return res