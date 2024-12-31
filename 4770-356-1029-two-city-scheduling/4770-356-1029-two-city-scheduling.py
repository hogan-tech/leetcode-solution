# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costList = [[costB - costA, costA, costB] for costA, costB in costs]
        costList.sort()
        result = 0
        for i in range(n):
            result += costList[i][2] + costList[len(costs) - i - 1][1]
        return result


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(Solution().twoCitySchedCost(costs))
costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(Solution().twoCitySchedCost(costs))
costs = [[515, 563], [451, 713], [537, 709], [343, 819],
         [855, 779], [457, 60], [650, 359], [631, 42]]
print(Solution().twoCitySchedCost(costs))
