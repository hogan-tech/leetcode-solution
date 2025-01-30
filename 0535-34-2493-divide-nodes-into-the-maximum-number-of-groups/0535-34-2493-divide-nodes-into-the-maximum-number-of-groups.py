# time complexity: O(n*(n+m))
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        parent = [-1] * n
        depth = [0] * n
        for edge in edges:
            adjList[edge[0] - 1].append(edge[1] - 1)
            adjList[edge[1] - 1].append(edge[0] - 1)
            self.union(edge[0] - 1, edge[1] - 1, parent, depth)
        numOfGroupsForComponent = {}
        for node in range(n):
            numberOfGroups = self.getNumberOfGroups(adjList, node, n)
            if numberOfGroups == -1:
                return -1
            root_node = self.find(node, parent)
            numOfGroupsForComponent[root_node] = max(
                numOfGroupsForComponent.get(root_node, 0), numberOfGroups
            )

        total_number_of_groups = sum(numOfGroupsForComponent.values())
        return total_number_of_groups

    def getNumberOfGroups(self, adjList, src_node, n):
        nodesQueue = deque()
        layerSeen = [-1] * n
        nodesQueue.append(src_node)
        layerSeen[src_node] = 0
        deepestLayer = 0

        while nodesQueue:
            numOfNodesInLayer = len(nodesQueue)
            for _ in range(numOfNodesInLayer):
                current_node = nodesQueue.popleft()
                for neighbor in adjList[current_node]:

                    if layerSeen[neighbor] == -1:
                        layerSeen[neighbor] = deepestLayer + 1
                        nodesQueue.append(neighbor)
                    else:

                        if layerSeen[neighbor] == deepestLayer:
                            return -1
            deepestLayer += 1
        return deepestLayer

    def find(self, node, parent):
        while parent[node] != -1:
            node = parent[node]
        return node

    def union(self, node1, node2, parent, depth):
        node1 = self.find(node1, parent)
        node2 = self.find(node2, parent)

        if node1 == node2:
            return

        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1
        parent[node2] = node1

        if depth[node1] == depth[node2]:
            depth[node1] += 1


n = 6
edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
print(Solution().magnificentSets(n, edges))
n = 3
edges = [[1, 2], [2, 3], [3, 1]]
print(Solution().magnificentSets(n, edges))
