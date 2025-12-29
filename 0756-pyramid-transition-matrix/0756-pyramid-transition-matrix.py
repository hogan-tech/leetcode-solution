# time complexity: O(A ^ N)
# space complexity: O(n^2)
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tab = defaultdict(set)
        for u, v, w in allowed:
            tab[u, v].add(w)

        def add_neighbor(node):
            res = ['']
            for i in range(1, len(node)):
                eles = tab[(node[i - 1], node[i])]
                if eles:
                    res = [a + e for e in eles for a in res]
                else:
                    return []
            return res
        
        
        visited = set()

        def dfs(node):
            if len(node) == 1:
                return True
            if node in visited:
                return False

            for nxt in add_neighbor(node):
                if dfs(nxt):
                    return True

            visited.add(node)
            return False

        return dfs(bottom)


bottom = "BCD"
allowed = ["BCC", "CDE", "CEA", "FFF"]
print(Solution().pyramidTransition(bottom, allowed))
bottom = "AAAA"
allowed = ["AAB", "AAC", "BCD", "BBE", "DEF"]
print(Solution().pyramidTransition(bottom, allowed))
