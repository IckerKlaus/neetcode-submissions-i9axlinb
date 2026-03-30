class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lenght = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.lenght == self.capacity:
            self.resize()
        self.arr[self.lenght] = n
        self.lenght += 1

    def popback(self) -> int:
        if self.lenght > 0:
            self.lenght -= 1
        return self.arr[self.lenght]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        myArr = [0] * self.capacity
        for i in range(self.lenght):
            myArr[i] = self.arr[i]
        self.arr = myArr

    def getSize(self) -> int:
        return self.lenght
        
    def getCapacity(self) -> int:
        return self.capacity
