# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW = len(box)
        COL = len(box[0])

        for i in range(ROW):
            emptyPos = COL - 1
            for j in range(COL - 1, -1, -1):
                if box[i][j] == '*':
                    emptyPos = j - 1
                elif box[i][j] == '#':
                    box[i][j], box[i][emptyPos] = '.', '#'
                    emptyPos -= 1

        rotatedBox = [[''] * ROW for _ in range(COL)]
        for i in range(ROW):
            for j in range(COL):
                rotatedBox[j][ROW - 1 - i] = box[i][j]

        return rotatedBox


box = [["#", ".", "#"]]
print(Solution().rotateTheBox(box))

box = [["#", ".", "*", "."],
       ["#", "#", "*", "."]]
print(Solution().rotateTheBox(box))

box = [["#", "#", "*", ".", "*", "."],
       ["#", "#", "#", "*", ".", "."],
       ["#", "#", "#", ".", "#", "."]]
print(Solution().rotateTheBox(box))
