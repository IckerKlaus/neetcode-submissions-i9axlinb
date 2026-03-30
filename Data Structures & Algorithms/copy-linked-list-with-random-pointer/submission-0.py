"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = {None : None}

        cur = head
        while cur:
            node = Node(cur.val)
            oldtonew[cur] = node
            cur = cur.next

        cur = head
        while cur:
            node = oldtonew[cur]
            node.next = oldtonew[cur.next]
            node.random = oldtonew[cur.random]
            cur = cur.next
        
        return oldtonew[head]