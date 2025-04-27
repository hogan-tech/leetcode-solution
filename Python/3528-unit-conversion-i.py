# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(conversions) + 1
        graph = defaultdict(list)

        for src, tgt, factor in conversions:
            graph[src].append((tgt, factor))

        result = [0] * n
        result[0] = 1

        def dfs(node):
            for neighbor, factor in graph[node]:
                result[neighbor] = result[node] * factor % MOD
                dfs(neighbor)

        dfs(0)
        return result


conversions = [[0, 1, 2], [1, 2, 3]]
print(Solution().baseUnitConversions(conversions))
conversions = [[0, 1, 2], [0, 2, 3], [1, 3, 4],
               [1, 4, 5], [2, 5, 2], [4, 6, 3], [5, 7, 4]]
print(Solution().baseUnitConversions(conversions))
