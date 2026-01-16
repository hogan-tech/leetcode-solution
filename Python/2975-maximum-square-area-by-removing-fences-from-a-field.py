# time complexity: O(h^2 + v^2)
# space complexity: O(h^2 + v^2)
from typing import List


class Solution:
    def getEdges(self, fences: List[int], border: int) -> set:
        points = sorted([1] + fences + [border])
        return {
            points[j] - points[i]
            for i in range(len(points))
            for j in range(i + 1, len(points))
        }

    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7
        hEdges = self.getEdges(hFences, m)
        vEdges = self.getEdges(vFences, n)

        maxEdge = max(hEdges & vEdges, default=0)
        return (maxEdge * maxEdge) % MOD if maxEdge else -1


m = 4
n = 3
hFences = [2, 3]
vFences = [2]
print(Solution().maximizeSquareArea(m, n, hFences, vFences))
m = 6
n = 7
hFences = [2]
vFences = [4]
print(Solution().maximizeSquareArea(m, n, hFences, vFences))
