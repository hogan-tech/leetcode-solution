# time complexity: O(n^3)
# space complexity: O(1)
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        n = len(points)

        for i in range(n):
            pointA = points[i]
            for j in range(n):
                pointB = points[j]
                if i == j or not (pointA[0] <= pointB[0] and pointA[1] >= pointB[1]):
                    continue
                if n == 2:
                    result += 1
                    continue
                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue
                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0])
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1])
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    result += 1
        return result


points = [[1, 1], [2, 2], [3, 3]]
print(Solution().numberOfPairs(points))
points = [[6, 2], [4, 4], [2, 6]]
print(Solution().numberOfPairs(points))
points = [[3, 1], [1, 3], [1, 1]]
print(Solution().numberOfPairs(points))
