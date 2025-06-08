# time complexity: O(n)
# space complexity: O(logn)
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographicalNumbers = []
        for start in range(1, 10):
            self.generateLexicalNumbers(start, n, lexicographicalNumbers)
        return lexicographicalNumbers

    def generateLexicalNumbers(self, currentNumber: int, limit: int, result: List[int]):
        if currentNumber > limit:
            return
        result.append(currentNumber)
        for nextDigit in range(10):
            nextNumber = currentNumber * 10 + nextDigit
            if nextNumber <= limit:
                self.generateLexicalNumbers(nextNumber, limit, result)
            else:
                break


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, n + 1):
            result.append(str(i))
        result.sort()
        return [int(num) for num in result]


n = 13
print(Solution().lexicalOrder(n))
n = 2
print(Solution().lexicalOrder(n))
