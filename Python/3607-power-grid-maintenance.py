# time complexity: O((c + q) * α(c))
# space complexity: O(c)
from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for u, v in connections:
            union(u, v)

        groupMembers = defaultdict(list)
        for node in range(1, c + 1):
            root = find(node)
            groupMembers[root].append(node)

        componentMap = dict()
        for root, members in groupMembers.items():
            componentMap[root] = SortedSet(members)

        nodeToRoot = {node: find(node) for node in range(1, c + 1)}

        online = [True] * (c + 1)

        result = []

        for type, x in queries:
            if type == 1:  
                if online[x]:
                    result.append(x)
                else:
                    root = nodeToRoot[x]
                    candidates = componentMap[root]
                    if candidates:
                        result.append(candidates[0])
                    else:
                        result.append(-1)
            else:  
                if online[x]:
                    online[x] = False
                    root = nodeToRoot[x]
                    componentMap[root].discard(x)

        return result



c = 5
connections = [[1, 2], [2, 3], [3, 4], [4, 5]]
queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
print(Solution().processQueries(c, connections, queries))
c = 3
connections = []
queries = [[1, 1], [2, 1], [1, 1]]
print(Solution().processQueries(c, connections, queries))
