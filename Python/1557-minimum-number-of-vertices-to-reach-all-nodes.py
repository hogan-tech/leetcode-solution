# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        allNodes = set(list(i for i in range(n)))
        destinations = set(list(des for _, des in edges))
        return list(allNodes - destinations)


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
print(Solution().findSmallestSetOfVertices(n, edges))
n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
print(Solution().findSmallestSetOfVertices(n, edges))
