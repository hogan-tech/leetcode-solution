# time complexity: O(1)
# space complexity: O(n)
from collections import defaultdict


class Logger:

    def __init__(self):
        self.logDict = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logDict:
            self.logDict[message] = timestamp + 10
            return True
        else:
            if timestamp < self.logDict[message]:
                return False
            else:
                self.logDict[message] = timestamp + 10
                return True


# Your Logger object will be instantiated and called as such:
obj = Logger()
print(obj.shouldPrintMessage(1, "foo"))
print(obj.shouldPrintMessage(2, "bar"))
print(obj.shouldPrintMessage(3, "foo"))
print(obj.shouldPrintMessage(8, "bar"))
print(obj.shouldPrintMessage(10, "foo"))
print(obj.shouldPrintMessage(11, "foo"))
