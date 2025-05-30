# time complexity: O(v+e)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(startNode: int, distanceList: List[int]):

            queue = deque([startNode])
            visited = [False for _ in range(len(edges))]
            distanceList[startNode] = 0
            while queue:
                currNode = queue.popleft()
                if visited[currNode]:
                    return
                visited[currNode] = True
                nextNode = edges[currNode]
                if nextNode != -1 and not visited[nextNode]:
                    distanceList[nextNode] = distanceList[currNode] + 1
                    queue.append(nextNode)

        distanceNodeOne = [float('inf') for _ in range(len(edges))]
        distanceNodeTwo = [float('inf') for _ in range(len(edges))]

        bfs(node1, distanceNodeOne)
        bfs(node2, distanceNodeTwo)

        minNode = -1
        minDistance = float('inf')
        for currNode in range(len(edges)):
            if minDistance > max(distanceNodeOne[currNode], distanceNodeTwo[currNode]):
                minNode = currNode
                minDistance = max(
                    distanceNodeOne[currNode], distanceNodeTwo[currNode])

        return minNode


edges = [2, 2, 3, -1]
node1 = 0
node2 = 1
print(Solution().closestMeetingNode(edges, node1, node2))
edges = [1, 2, -1]
node1 = 0
node2 = 2
print(Solution().closestMeetingNode(edges, node1, node2))
