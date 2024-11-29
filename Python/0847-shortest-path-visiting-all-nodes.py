from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n = len(graph)
        endingMask = (1<<n) - 1
        queue = [(node, 1<< node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            nextQueue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    nextMask = mask | (1 << neighbor)
                    if nextMask == endingMask:
                        return 1 + steps
                    if (neighbor , nextMask) not in seen:
                        seen.add((neighbor, nextMask))
                        nextQueue.append((neighbor, nextMask))
            steps += 1
            queue = nextQueue
        return steps


graph = [[1, 2, 3], [0], [0], [0]]
