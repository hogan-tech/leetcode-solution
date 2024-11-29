from collections import defaultdict, deque
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def tp_sort(g, indegree):
            visited = []
            q = deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                node = q.popleft()
                visited.append(node)
                for v in g[node]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return visited

        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_indegree = [0] * n
        item_graph = defaultdict(list)

        group_indegree = [0] * group_id
        group_graph = defaultdict(list)

        for i in range(n):
            for item in beforeItems[i]:
                item_graph[item].append(i)
                item_indegree[i] += 1
                if group[i] != group[item]:
                    group_indegree[group[i]] += 1
                    group_graph[group[item]].append(group[i])

        item_sorted = tp_sort(item_graph, item_indegree)
        group_sorted = tp_sort(group_graph, group_indegree)

        if len(item_sorted) != n or len(group_sorted) != group_id:
            return []

        ans = []
        umap = defaultdict(list)

        for elem in item_sorted:
            umap[group[elem]].append(elem)

        for gp_elem in group_sorted:
            ans.extend(umap[gp_elem])

        return ans


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]


print(Solution().sortItems(n, m, group, beforeItems))
