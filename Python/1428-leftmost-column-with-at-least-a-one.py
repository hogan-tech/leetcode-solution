# time complexity: O(n * m)
# space complexity: O(1)
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[int]:

import bisect


class Row:
    def __init__(self, row, matrix):
        self.id = row
        self.matrix = matrix

    def __getitem__(self, j):
        return self.matrix.get(self.id, j)

    def __len__(self):
        return self.matrix.dimensions()[1]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()

        s = bisect.bisect_left(Row(0, binaryMatrix), 1)
        for i in range(1, n):
            s = min(s, bisect.bisect_left(Row(i, binaryMatrix), 1))

        if s == m:
            return -1
        return s
