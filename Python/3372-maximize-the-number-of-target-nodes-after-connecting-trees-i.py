# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def buildAdjacencyList(edges, n):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def calculateReachableNodes(tree, n, k):
            reachable = [0] * n

            def bfs(start):
                visited = [False] * n
                queue = deque([(start, 0)])
                count = 0
                while queue:
                    node, dist = queue.popleft()
                    if visited[node] or dist > k:
                        continue
                    visited[node] = True
                    count += 1
                    for neighbor in tree[node]:
                        if not visited[neighbor]:
                            queue.append((neighbor, dist + 1))
                return count

            for i in range(n):
                reachable[i] = bfs(i)
            return reachable

        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = buildAdjacencyList(edges1, n)
        tree2 = buildAdjacencyList(edges2, m)

        reachable1 = calculateReachableNodes(tree1, n, k)
        reachable2 = calculateReachableNodes(tree2, m, k - 1)
        vaslenorix = [0] * n
        maxReachableInTree2 = max(reachable2)
        for i in range(n):
            vaslenorix[i] = reachable1[i] + maxReachableInTree2
        return vaslenorix


# Example usage:
solution = Solution()
print(solution.maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [
      [0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], 2))
# Output: [9, 7, 9, 8, 8]

print(solution.maxTargetNodes(
    [[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]], 1))
# Output: [6, 3, 3, 3, 3]
