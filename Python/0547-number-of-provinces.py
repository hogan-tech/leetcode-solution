# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = 0
        seen = set()

        def dfs(city: int):
            for neighbor, connected in enumerate(isConnected[city]):
                if neighbor not in seen and connected == 1:
                    seen.add(neighbor)
                    dfs(neighbor)

        for city in range(len(isConnected)):
            if city not in seen:
                seen.add(city)
                dfs(city)
                result += 1
        return result


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
