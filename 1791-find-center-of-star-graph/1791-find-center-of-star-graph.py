# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeSet = {}
        for edge in edges:
            for item in edge:
                if item in edgeSet:
                    edgeSet[item] += 1
                else:
                    edgeSet[item] = 1
        for node, count in edgeSet.items():
            if count == len(edges):
                return node
        return -1


edges = [[1, 2], [2, 3], [4, 2]]
print(Solution().findCenter(edges))
