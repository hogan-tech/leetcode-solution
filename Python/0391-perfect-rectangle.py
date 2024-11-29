# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        pointDict = defaultdict(int)
        finalX1 = float('inf')
        finalY1 = float('inf')
        finalX2 = float('-inf')
        finalY2 = float('-inf')
        finalArea = 0
        tempArea = 0
        for x1, y1, x2, y2 in rectangles:
            finalX1 = min(finalX1, x1)
            finalY1 = min(finalY1, y1)
            finalX2 = max(finalX2, x2)
            finalY2 = max(finalY2, y2)
            tempArea += (abs(x1 - x2) * abs(y1 - y2))
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                pointDict[point] += 1
        finalArea = (finalX2 - finalX1) * (finalY2 - finalY1)
        if finalArea != tempArea:
            return False

        finals = [(finalX1, finalY1), (finalX1, finalY2),
                  (finalX2, finalY1), (finalX2, finalY2)]

        for finalPoint in finals:
            if pointDict[finalPoint] != 1:
                print(finalPoint, pointDict[finalPoint])
                return False

        for point, count in pointDict.items():
            if point not in finals and count not in [2, 4]:
                return False
        return True


rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [
    3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
print(Solution().isRectangleCover(rectangles))
rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
print(Solution().isRectangleCover(rectangles))
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
print(Solution().isRectangleCover(rectangles))
