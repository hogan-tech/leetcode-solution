# time complexity: O(n)
# space complexity: O(n)
from collections import deque


class Solution:
    def clumsy(self, n: int) -> int:
        operationFuncs = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
        }
        operations = ['*', '/', '+', '-']
        operationQue = deque()
        numQue = deque()
        count = 0
        temp = n
        for num in range(n - 1, 0, -1):
            currOperation = operations[count % 4]
            if count % 4 != 0 and count % 4 != 1:
                operationQue.append(currOperation)
                numQue.append(temp)
                temp = num
            else:
                temp = operationFuncs[currOperation](temp, num)
            count += 1
        numQue.append(temp)
        result = numQue.popleft()
        while operationQue:
            currOperation = operationQue.popleft()
            currNum = numQue.popleft()
            result = operationFuncs[currOperation](result, currNum)
        return result


n = 4
print(Solution().clumsy(n))
n = 10
print(Solution().clumsy(n))
