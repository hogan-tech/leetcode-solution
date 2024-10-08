# time complexity: O(2^V * V)
# for the DAG need O(2^V - 1)
# space complexity: O(V)
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        result = []

        def dfs(currNode):
            path.append(currNode)
            if currNode == len(graph) - 1:
                result.append(path.copy())
                return
            nextNodes = graph[currNode]
            for nextNode in nextNodes:
                dfs(nextNode)
                path.pop()

        dfs(0)
        return result


graph = [[1, 2], [3], [3], []]
print(Solution().allPathsSourceTarget(graph))
