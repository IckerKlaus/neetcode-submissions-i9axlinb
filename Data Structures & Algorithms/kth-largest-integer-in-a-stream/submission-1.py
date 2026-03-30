class MinHeap:
    def __init__(self):
        self.heap = [0]

    def __len__(self):
        return len(self.heap) - 1

    def top(self):
        return self.heap[1]
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def heapreplace(self, val):
        old_root = self.heap[1]
        self.heap[1] = val
        i = 1
        n = len(self.heap)

        while 2 * i < n:
            left = 2 * i
            right = left + 1

            child = right if right < n and self.heap[right] < self.heap[left] else left
            if self.heap[i] <= self.heap[child]:
                break
            
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
        return old_root

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = MinHeap()
        self.k = k

        for num in nums:
            if len(self.h) < k:
                self.h.push(num)
            else:
                if num > self.h.top():
                    self.h.heapreplace(num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            self.h.push(val)
        elif val > self.h.top():
            self.h.heapreplace(val)
        return self.h.top()




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)