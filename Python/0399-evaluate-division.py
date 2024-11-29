# time complexity: O(m*n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        def backtrack(currNode: str, targetNode: str, accProduct: int, visited: set):
            visited.add(currNode)
            ret = -1.0
            neighbors = graph[currNode]
            if targetNode in neighbors:
                ret = accProduct * neighbors[targetNode]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack(neighbor, targetNode,
                                    accProduct * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(currNode)
            return ret

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = backtrack(dividend, divisor, 1, visited)
            results.append(ret)

        return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Solution().calcEquation(equations, values, queries))
