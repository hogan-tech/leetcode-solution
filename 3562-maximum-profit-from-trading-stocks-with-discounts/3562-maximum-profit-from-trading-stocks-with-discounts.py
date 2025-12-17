# time complexity: O(n * b ^ 2)
# space complexity: O(n * b)
from typing import List


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        g = [[] for _ in range(n)]
        for e in hierarchy:
            g[e[0] - 1].append(e[1] - 1)

        def dfs(u: int):
            cost = present[u]
            dCost = present[u] // 2

            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            subProfit0 = [0] * (budget + 1)
            subProfit1 = [0] * (budget + 1)
            uSize = cost

            for v in g[u]:
                child_dp0, child_dp1, vSize = dfs(v)
                uSize += vSize
                for i in range(budget, -1, -1):
                    for sub in range(min(vSize, i) + 1):
                        if i - sub >= 0:
                            subProfit0[i] = max(
                                subProfit0[i],
                                subProfit0[i - sub] + child_dp0[sub],
                            )
                            subProfit1[i] = max(
                                subProfit1[i],
                                subProfit1[i - sub] + child_dp1[sub],
                            )

            for i in range(budget + 1):
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]
                if i >= dCost:
                    dp1[i] = max(
                        subProfit0[i], subProfit1[i - dCost] +
                        future[u] - dCost
                    )
                if i >= cost:
                    dp0[i] = max(
                        subProfit0[i], subProfit1[i - cost] + future[u] - cost
                    )

            return dp0, dp1, uSize

        return dfs(0)[0][budget]


n = 2
present = [1, 2]
future = [4, 3]
hierarchy = [[1, 2]]
budget = 3
print(Solution().maxProfit(n, present, future, hierarchy, budget))
n = 2
present = [3, 4]
future = [5, 8]
hierarchy = [[1, 2]]
budget = 4
print(Solution().maxProfit(n, present, future, hierarchy, budget))
n = 3
present = [4, 6, 8]
future = [7, 9, 11]
hierarchy = [[1, 2], [1, 3]]
budget = 10
print(Solution().maxProfit(n, present, future, hierarchy, budget))
n = 3
present = [5, 2, 3]
future = [8, 5, 6]
hierarchy = [[1, 2], [2, 3]]
budget = 7
