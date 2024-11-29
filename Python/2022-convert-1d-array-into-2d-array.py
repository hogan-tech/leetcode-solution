# time complexity: O(m*n)
# space complexity: O(1)
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(m)]
        idx = 0
        if m * n != len(original):
            return []
        for row in range(m):
            for col in range(n):
                result[row][col] = original[idx]
                idx += 1
        return result


original = [1, 2, 3, 4]
m = 2
n = 2
print(Solution().construct2DArray(original, m, n))
