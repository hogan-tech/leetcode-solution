# time complexity: O(V+E)
# space complexity: O(V+E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjMatrix = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        for pair in pairs:
            start, end = pair
            adjMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        if startNode == -1:
            startNode = pairs[0][0]

        def visit(node):
            while adjMatrix[node]:
                nextNode = adjMatrix[node].popleft()
                visit(nextNode)
            result.append(node)

        visit(startNode)

        result.reverse()
        pairedResult = [[result[i-1], result[i]]
                        for i in range(1, len(result))]
        return pairedResult


pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
print(Solution().validArrangement(pairs))
