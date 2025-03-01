# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        for i in range(len(original)):
            currNum = original[i]
            bounds[i][0] -= currNum
            bounds[i][1] -= currNum

        left = -float('inf')
        right = float('inf')
        for bound in bounds:
            left = max(left, bound[0])
            right = min(right, bound[1])

        return right - left + 1 if right >= left else 0


original = [1, 2, 3, 4]
bounds = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(Solution().countArrays(original, bounds))
original = [1, 2, 3, 4]
bounds = [[1, 10], [2, 9], [3, 8], [4, 7]]
print(Solution().countArrays(original, bounds))
original = [1, 2, 1, 2]
bounds = [[1, 3], [2, 4], [3, 3], [2, 4]]
print(Solution().countArrays(original, bounds))
