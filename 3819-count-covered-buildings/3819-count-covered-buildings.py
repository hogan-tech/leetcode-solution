# time complexity: O(nlogn)
# space complexity: O(n)
import bisect
from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)

        for x, y in buildings:
            rowMap[x].append(y)
            colMap[y].append(x)

        for row in rowMap:
            rowMap[row].sort()
        for col in colMap:
            colMap[col].sort()

        result = 0
        for x, y in buildings:
            row = rowMap[x]
            col = colMap[y]

            rowIdx = bisect.bisect_left(row, y)
            hasLeft = rowIdx > 0
            hasRight = rowIdx < len(row) - 1

            colIdx = bisect.bisect_left(col, x)
            hasAbove = colIdx > 0
            hasBelow = colIdx < len(col) - 1

            if hasLeft and hasRight and hasAbove and hasBelow:
                result += 1

        return result


n = 3
buildings = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
print(Solution().countCoveredBuildings(n, buildings))
n = 3
buildings = [[1, 1], [1, 2], [2, 1], [2, 2]]
print(Solution().countCoveredBuildings(n, buildings))
n = 5
buildings = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
print(Solution().countCoveredBuildings(n, buildings))
