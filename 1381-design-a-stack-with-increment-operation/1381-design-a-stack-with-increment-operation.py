class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.capacity:
            print(self.stack)
        else:
            self.stack.append(x)
            print(self.stack)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


stk = CustomStack(2)
stk.push(34)
print(stk.pop())
stk.increment(8, 100)
print(stk.pop())
stk.increment(9, 91)
stk.push(84)
stk.increment(10, 93)
stk.increment(6, 45)
stk.increment(10, 4)

