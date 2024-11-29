from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: []for i in range(1, n+1)}
        inCount = {i: 0 for i in range(1, n+1)}
        for startNode, endNode in relations:
            graph[startNode].append(endNode)
            inCount[endNode] += 1
        queue = []
        for node in graph:
            if inCount[node] == 0:
                queue.append(node)

        step = 0
        studiedCount = 0

        while queue:
            step += 1
            nextQueue = []
            for node in queue:
                studiedCount += 1
                endNodeS = graph[node]
                for endNode in endNodeS:
                    inCount[endNode] -= 1
                    if inCount[endNode] == 0:
                        nextQueue.append(endNode)
            queue = nextQueue

        return step if studiedCount == n else -1


n = 3
relations = [[1, 3], [2, 3]]
print(Solution().minimumSemesters(n, relations))
