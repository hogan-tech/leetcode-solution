# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.bobPath = {}
        self.visited = []
        self.tree = []

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        maxIncome = float("-inf")
        self.tree = [[] for _ in range(n)]
        self.bobPath = {}
        self.visited = [False] * n
        queue = deque([(0, 0, 0)])

        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        self.findBobPath(bob, 0)

        self.visited = [False] * n
        while queue:
            currNode, time, income = queue.popleft()

            if (
                currNode not in self.bobPath
                or time < self.bobPath[currNode]
            ):
                income += amount[currNode]

            elif time == self.bobPath[currNode]:
                income += amount[currNode] // 2

            if len(self.tree[currNode]) == 1 and currNode != 0:
                maxIncome = max(maxIncome, income)

            for adjacentNode in self.tree[currNode]:
                if not self.visited[adjacentNode]:
                    queue.append((adjacentNode, time + 1, income))

            self.visited[currNode] = True

        return maxIncome

    def findBobPath(self, currNode, time):

        self.bobPath[currNode] = time
        self.visited[currNode] = True

        if currNode == 0:
            return True

        for adjacentNode in self.tree[currNode]:
            if not self.visited[adjacentNode]:
                if self.findBobPath(adjacentNode, time + 1):
                    return True

        self.bobPath.pop(currNode, None)
        return False


edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]
print(Solution().mostProfitablePath(edges, bob, amount))
edges = [[0, 1]]
bob = 1
amount = [-7280, 2350]
print(Solution().mostProfitablePath(edges, bob, amount))
