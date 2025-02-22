# time complexity: O(m*n)
# space complexity: O(n)
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROW = len(mat)
        intersectionSet = set(mat[0])
        for r in range(1, ROW):
            intersectionSet = intersectionSet.intersection(set(mat[r]))
        return list(intersectionSet)[0] if len(intersectionSet) > 0 else -1


mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
print(Solution().smallestCommonElement(mat))
mat = [[1, 2, 3], [2, 3, 4], [2, 3, 5]]
print(Solution().smallestCommonElement(mat))
