# time complexity: O(n+m)
# space complexity: O(1)
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        firstIdx = 0
        secondIdx = 0
        intersections = []
        while firstIdx < len(firstList) and secondIdx < len(secondList):
            start = max(firstList[firstIdx][0], secondList[secondIdx][0])
            end = min(firstList[firstIdx][1], secondList[secondIdx][1])

            if start <= end:
                intersections.append([start, end])
            if firstList[firstIdx][1] < secondList[secondIdx][1]:
                firstIdx += 1
            else:
                secondIdx += 1

        return intersections


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().intervalIntersection(firstList, secondList))

firstList = [[1, 3], [5, 9]]
secondList = []
print(Solution().intervalIntersection(firstList, secondList))
