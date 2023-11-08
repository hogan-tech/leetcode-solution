#time complexity: O(n)
#space complexity: O(1)
from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def distance(a: List[int], b: List[int]):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        totalDist = 0
        d = -100000
        for nut in nuts:
            totalDist += distance(nut, tree) * 2
            d = max(d, distance(nut, tree) - distance(nut, squirrel))
        return totalDist - d


height = 5
width = 7
tree = [2, 2]
squirrel = [4, 4]
nuts = [[3, 0], [2, 5]]

print(Solution().minDistance(height, width, tree, squirrel, nuts))
