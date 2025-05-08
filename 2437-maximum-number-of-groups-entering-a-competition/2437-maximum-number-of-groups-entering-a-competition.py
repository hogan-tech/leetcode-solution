# time complexity: O(logn)
# space complexity: O(1)
from math import sqrt
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int((sqrt(1 + 8 * len(grades)) - 1)/2)


grades = [10, 6, 12, 7, 3, 5]
print(Solution().maximumGroups(grades))
grades = [8, 8]
print(Solution().maximumGroups(grades))
