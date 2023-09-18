from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for row in range(len(mat)):
            result.append([row, sum(mat[row])])
        sortedList = sorted(result, key=lambda x: x[1])
        result = []
        for row in range(len(mat)):
            result.append(sortedList[row][0])
        return result[:k]


mat = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
k = 1


print(Solution().kWeakestRows(mat, k))
