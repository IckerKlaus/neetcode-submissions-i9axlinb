class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, val):
        new_node = Node(val)

        if not self.right:
            self.left = self.right = new_node
        else:
            self.right.next = new_node
            self.right = new_node

    def dequeue(self):
        if not self.left:
            return None
        
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val
    
    def is_empty(self):
        return self.left is None
    
    def front(self):
        return self.left.val if self.left else None
    
    def printQueue(self):
        curr = self.left
        while curr:
            print(curr.val, "-> ", end="")
            curr = curr.next
        print()

class MyStack:
    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def push(self, x: int) -> None:
        self.q2.enqueue(x)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.front()

    def empty(self) -> bool:
        return self.q1.is_empty()

    def printStack(self):
        print("Stack (top->bottom): ", end="")
        self.q1.printQueue()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()