from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = [0] * (len(differences) + 1)
        minNum = 0
        maxNum = 0
        for i in range(1, len(differences) + 1):
            prefix[i] = prefix[i - 1] + differences[i - 1]
            minNum = min(minNum, prefix[i])
            maxNum = max(maxNum, prefix[i])
        
        lowerBound = lower - minNum
        upperBound = upper - maxNum
        
        return upperBound - lowerBound + 1 if upperBound >= lowerBound else 0


differences = [1, -3, 4]
lower = 1
upper = 6
print(Solution().numberOfArrays(differences, lower, upper))
differences = [3, -4, 5, 1, -2]
lower = -4
upper = 5
print(Solution().numberOfArrays(differences, lower, upper))
differences = [4, -7, 2]
lower = 3
upper = 6
print(Solution().numberOfArrays(differences, lower, upper))
