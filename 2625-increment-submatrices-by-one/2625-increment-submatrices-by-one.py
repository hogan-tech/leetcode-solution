# time complexity: O(n^2)
# space complexity: O(n^2)
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for startR, startC, endR, endC in queries:
            prefix[startR][startC] += 1
            prefix[endR + 1][startC] -= 1
            prefix[startR][endC + 1] -= 1
            prefix[endR + 1][endC + 1] += 1
        
        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else result[r - 1][c]
                left = 0 if c == 0 else result[r][c - 1]
                leftTop = 0 if r == 0 or c == 0 else result[r - 1][c - 1]
                result[r][c] = prefix[r][c] + top + left - leftTop
            
        return result


n = 3
queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
print(Solution().rangeAddQueries(n, queries))
n = 2
queries = [[0, 0, 1, 1]]
print(Solution().rangeAddQueries(n, queries))
