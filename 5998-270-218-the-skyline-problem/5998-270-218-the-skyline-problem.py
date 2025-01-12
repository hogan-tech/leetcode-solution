# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, num):
        if num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    def union(self, x, y):
        self.parent[x] = self.parent[y]


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        coordinates = sorted(
            list(set([x for building in buildings for x in building[:2]])))

        n = len(coordinates)
        heights = [0] * n
        indexMap = {x: idx for idx, x in enumerate(coordinates)}
        buildings.sort(key=lambda x: -x[2])
        skyline = []
        uf = UnionFind(n)

        for leftX, rightX, height in buildings:
            left, right = indexMap[leftX], indexMap[rightX]

            while left < right:
                left = uf.find(left)
                if left < right:
                    uf.union(left, right)
                    heights[left] = height
                    left += 1

        for i in range(n):
            if i == 0 or heights[i] != heights[i - 1]:
                skyline.append([coordinates[i], heights[i]])
        return skyline


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(Solution().getSkyline(buildings))
buildings = [[0, 2, 3], [2, 5, 3]]
print(Solution().getSkyline(buildings))
