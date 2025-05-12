# time complexity: O(n^3)
# space complexity: O(n)
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        numsSet = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2:
                        continue
                    validNum = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if validNum not in numsSet:
                        numsSet.add(validNum)
                        result.append(validNum)
        result.sort()
        return result


digits = [2, 1, 3, 0]
print(Solution().findEvenNumbers(digits))
digits = [2, 2, 8, 8, 2]
print(Solution().findEvenNumbers(digits))
digits = [3, 7, 5]
print(Solution().findEvenNumbers(digits))
