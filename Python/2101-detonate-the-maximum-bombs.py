# time complexity: O(n^3)
# space complexity: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        result = 0
        graph = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, r = bombs[i]
                xj, yj, _ = bombs[j]
                if r**2 >= (xi-xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def dfs(curr, visited):
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return len(visited)

        for i in range(n):
            visited = set()
            result = max(result, dfs(i, visited))
        return result


bombs = [[2, 1, 3], [6, 1, 4]]
print(Solution().maximumDetonation(bombs))
