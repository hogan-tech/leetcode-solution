from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for i in range(len(row)-1):
                row[i+1] += row[i]

        count = 0
        for t in range(len(matrix)):
            for b in range(t, -1, -1):
                if t == b:
                    cur = matrix[t][:]
                else:
                    cur = [cur[i]+matrix[b][i] for i in range(len(matrix[0]))]
                seen = {0: 1}
                for v in cur:
                    if v - target in seen:
                        count += seen[v - target]
                    seen[v] = seen.get(v, 0) + 1

        return count


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
print(Solution().numSubmatrixSumTarget(matrix, target))
