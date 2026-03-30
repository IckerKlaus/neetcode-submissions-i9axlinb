# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)
    
    def mergeSort(self, arr, l, r):
        if l > r:
            return None
        if l == r:
            return arr[l]
        m = (l + r) // 2
        left = self.mergeSort(arr, l, m)
        right = self.mergeSort(arr, m + 1, r)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        
        tail.next = a if a else b
        return dummy.next
