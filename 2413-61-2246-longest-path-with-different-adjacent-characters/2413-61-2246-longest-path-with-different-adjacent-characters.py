# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        indegree = [0] * n
        for node in range(1, n):
            indegree[parent[node]] += 1

        queue = deque()
        longestChains = [[0, 0] for _ in range(n)]
        longestPath = 1

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                longestChains[node][0] = 1

        while queue:
            currentNode = queue.popleft()
            parentNode = parent[currentNode]

            if parentNode != -1:
                longestChainFromCurr = longestChains[currentNode][0]

                if s[currentNode] != s[parentNode]:
                    if longestChainFromCurr > longestChains[parentNode][0]:
                        longestChains[parentNode][1] = longestChains[parentNode][0]
                        longestChains[parentNode][0] = longestChainFromCurr
                    elif longestChainFromCurr > longestChains[parentNode][1]:
                        longestChains[parentNode][1] = longestChainFromCurr

                longestPath = max(
                    longestPath, longestChains[parentNode][0] + longestChains[parentNode][1] + 1)

                indegree[parentNode] -= 1
                if indegree[parentNode] == 0:
                    longestChains[parentNode][0] += 1
                    queue.append(parentNode)
        return longestPath


parent = [-1, 0, 0, 1, 1, 2]
s = "abacbe"
print(Solution().longestPath(parent, s))
parent = [-1, 0, 0, 0]
s = "aabc"
print(Solution().longestPath(parent, s))
