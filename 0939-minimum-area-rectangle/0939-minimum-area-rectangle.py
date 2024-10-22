# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashMap = {}
        for singlePoint in points:
            if singlePoint[0] not in hashMap:
                hashMap[singlePoint[0]] = set()
            hashMap[singlePoint[0]].add(singlePoint[1])

        miniArea = float("inf")

        for i in range(len(points)):
            for j in range(len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 != x2 and y1 != y2:
                    if y2 in hashMap[x1] and y1 in hashMap[x2]:
                        miniArea = min(miniArea, abs(x1-x2) * abs(y1-y2))

        return miniArea if miniArea != float('inf') else 0


points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
print(Solution().minAreaRect(points))
