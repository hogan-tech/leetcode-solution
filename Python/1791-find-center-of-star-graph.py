# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return set(edges[0]).intersection(set(edges[1])).pop()


edges = [[1, 2], [2, 3], [4, 2]]
print(Solution().findCenter(edges))
edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
print(Solution().findCenter(edges))
