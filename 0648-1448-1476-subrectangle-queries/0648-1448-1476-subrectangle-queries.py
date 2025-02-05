# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.grid[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]


obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
print(obj.getValue(0, 2))
obj.updateSubrectangle(0, 0, 3, 2, 5)
print(obj.getValue(0, 2))
print(obj.getValue(3, 1))
obj.updateSubrectangle(3, 0, 3, 2, 10)
print(obj.getValue(3, 1))
print(obj.getValue(0, 2))
