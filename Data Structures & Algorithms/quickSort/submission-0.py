# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.realQuickSort(pairs, 0, len(pairs) - 1)
    
    def realQuickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot
        
        self.realQuickSort(arr, s, left - 1)

        self.realQuickSort(arr, left + 1, e)

        return arr













