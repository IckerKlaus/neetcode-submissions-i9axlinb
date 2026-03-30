# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        ll1 = ListNode(0)
        t1 = ll1

        while h1 and h2:
            if h1.val < h2.val:
                t1.next = h1
                h1 = h1.next
                t1 = t1.next
                t1.next = None
            else:
                t1.next = h2
                h2 = h2.next
                t1 = t1.next
                t1.next = None
        if h1:
            t1.next = h1
        if h2:
            t1.next = h2
        return ll1.next
