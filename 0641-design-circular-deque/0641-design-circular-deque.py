class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  
print(myCircularDeque.insertLast(2))  
print(myCircularDeque.insertFront(3)) 
print(myCircularDeque.insertFront(4)) 
print(myCircularDeque.getRear())      
print(myCircularDeque.isFull())       
print(myCircularDeque.deleteLast())   
print(myCircularDeque.insertFront(4)) 
print(myCircularDeque.getFront())     
