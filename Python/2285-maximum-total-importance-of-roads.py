# time complexity: (n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        degree.sort()
        total = 0
        for i in range(1, n+1):
            total += i * degree[i-1]
        return total


n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
print(Solution().maximumImportance(n, roads))
