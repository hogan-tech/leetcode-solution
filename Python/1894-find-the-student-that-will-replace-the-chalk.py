# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumChalk = 0
        for i in range(len(chalk)):
            sumChalk += chalk[i]
            if sumChalk > k:
                break
        k = k % sumChalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0


chalk = [32, 89, 30, 66, 25, 25, 80, 54, 21, 61, 96, 76, 74, 9, 9, 24, 31, 79, 45, 18, 8, 14, 30, 28, 85, 76, 69, 98, 80, 24, 23, 41, 47, 99, 4, 5, 88, 9, 17, 41, 52,
         61, 2, 54, 68, 40, 29, 33, 90, 63, 83, 88, 68, 57, 2, 93, 77, 40, 86, 11, 58, 85, 59, 100, 72, 98, 44, 1, 70, 83, 58, 43, 63, 74, 42, 8, 32, 80, 14, 90, 92, 15, 6]
k = 904272687
print(Solution().chalkReplacer(chalk, k))
