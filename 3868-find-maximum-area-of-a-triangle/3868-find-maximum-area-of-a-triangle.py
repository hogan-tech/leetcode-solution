# time complexity: O(n)
# space complexity: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:

        xGroup = defaultdict(list)
        yGroup = defaultdict(list)

        for x, y in coords:
            xGroup[x].append(y)
            yGroup[y].append(x)

        maxArea = 0

        for x in xGroup:
            ySame = xGroup[x]
            if len(ySame) >= 2:
                minY = min(ySame)
                maxY = max(ySame)
                base = maxY - minY
                pass

        for y in yGroup:
            xSame = yGroup[y]
            if len(xSame) >= 2:
                minX = min(xSame)
                maxX = max(xSame)
                base = maxX - minX
                pass

        if not coords:
            return -1

        allX = [x for x, _ in coords]
        allY = [y for _, y in coords]
        globalMinX = min(allX)
        globalMaxX = max(allX)
        globalMinY = min(allY)
        globalMaxY = max(allY)

        maxArea = 0

        for x in xGroup:
            ySame = xGroup[x]
            if len(ySame) < 2:
                continue
            minY = min(ySame)
            maxY = max(ySame)
            base = maxY - minY
            if len(xGroup) >= 2:
                height = max(globalMaxX - x, x - globalMinX)
                currArea = 0.5 * base * height
                if currArea > maxArea:
                    maxArea = currArea

        for y in yGroup:
            xSame = yGroup[y]
            if len(xSame) < 2:
                continue
            minX = min(xSame)
            maxX = max(xSame)
            base = maxX - minX
            if len(yGroup) >= 2:
                height = max(globalMaxY - y, y - globalMinY)
                currArea = 0.5 * base * height
                if currArea > maxArea:
                    maxArea = currArea

        return int(2 * maxArea) if maxArea != 0 else -1


coords = [[1, 1], [1, 2], [3, 2], [3, 3]]
print(Solution().maxArea(coords))
coords = [[1, 1], [2, 2], [3, 3]]
print(Solution().maxArea(coords))
