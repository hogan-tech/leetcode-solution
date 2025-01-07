class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # time complexity: O(n)
    # space complexity: O(n)
    def push(self, x: int) -> None:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    # time complexity: O(1)
    # space complexity: O(1)
    def pop(self) -> int:
        return self.stack1.pop()

    # time complexity: O(1)
    # space complexity: O(1)
    def peek(self) -> int:
        return self.stack1[-1]

    # time complexity: O(1)
    # space complexity: O(1)
    def empty(self) -> bool:
        return len(self.stack1) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
