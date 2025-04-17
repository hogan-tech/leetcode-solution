# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ColSet = set()
        RowSet = set()
        for _, tableNum, foodItem in orders:
            RowSet.add(int(tableNum))
            ColSet.add(foodItem)

        RowLen = len(RowSet)
        ColLen = len(ColSet)

        RowSortedList = sorted(list(RowSet))
        ColSortedList = sorted(list(ColSet))

        ColIdxMap = defaultdict(int)
        RowIdxMap = defaultdict(int)

        result = [["" for _ in range(ColLen + 1)] for _ in range(RowLen + 1)]
        result[0][0] += "Table"

        for i, val in enumerate(ColSortedList):
            ColIdxMap[val] = i
            result[0][i + 1] += val

        for i, val in enumerate(RowSortedList):
            RowIdxMap[str(val)] = i
            result[i + 1][0] += str(val)

        amountTable = [[0 for _ in range(ColLen)] for _ in range(RowLen)]

        for _, tableNum, foodItem in orders:
            colIdx = ColIdxMap[foodItem]
            rowIdx = RowIdxMap[tableNum]
            amountTable[rowIdx][colIdx] += 1

        for r in range(RowLen):
            for c in range(ColLen):
                result[r + 1][c + 1] += str(amountTable[r][c])

        return result


orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], [
    "Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
print(Solution().displayTable(orders))
