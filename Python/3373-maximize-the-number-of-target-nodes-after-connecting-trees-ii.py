# time complexity: O(n+m)
# space complexity: O(n+m)
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(node, parent, depth, children, color):
            result = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                if child == parent:
                    continue
                result += dfs(child, node, depth + 1, children, color)
            return result

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            result = dfs(0, -1, 0, children, color)
            return [result, n - result]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        resultList = [0] * n
        for i in range(n):
            resultList[i] = count1[color1[i]] + max(count2[0], count2[1])
        return resultList


edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
print(Solution().maxTargetNodes(edges1, edges2))
edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
edges2 = [[0, 1], [1, 2], [2, 3]]
print(Solution().maxTargetNodes(edges1, edges2))
