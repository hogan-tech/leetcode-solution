from math import sqrt
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        firstNum = num + 1
        secondNum = num + 2
        minDiff = float('inf')
        result = [0, 0]
        for i in range(1, int(sqrt(firstNum)) + 1):
            if firstNum % i == 0:
                divisor = firstNum // i
                diff = (divisor - i)
                if diff < minDiff:
                    minDiff = diff
                    result = [i, divisor]
                    
        for i in range(1, int(sqrt(secondNum)) + 1):
            if secondNum % i == 0:
                divisor = secondNum // i
                diff = (divisor - i)
                if diff < minDiff:
                    minDiff = diff
                    result = [i, divisor]
        
        return result


num = 8
print(Solution().closestDivisors(num))
num = 123
print(Solution().closestDivisors(num))
num = 999
print(Solution().closestDivisors(num))
