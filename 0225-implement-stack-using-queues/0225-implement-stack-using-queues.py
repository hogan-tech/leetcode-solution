from collections import deque


class MyStack:

    def __init__(self):
        self.val = deque()

    def push(self, x: int) -> None:
        self.val.append(x)

    def pop(self) -> int:
        return self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def empty(self) -> bool:
        return len(self.val) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
