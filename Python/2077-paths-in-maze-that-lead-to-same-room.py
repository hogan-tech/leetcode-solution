# time compelxity: O(n*m)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adjList = defaultdict(set)
        cycle = 0
        for room1, room2 in corridors:
            adjList[room1].add(room2)
            adjList[room2].add(room1)
            cycle += (len(adjList[room1].intersection(adjList[room2])))
        return cycle


n = 5
corridors = [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]
print(Solution().numberOfPaths(n, corridors))
n = 4
corridors = [[1, 2], [3, 4]]
print(Solution().numberOfPaths(n, corridors))
