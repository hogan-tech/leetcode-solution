# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        result = 0
        maxWeight = weight[0]
        i = 1
        while i < n:
            if weight[i] < maxWeight:
                result += 1
                if i + 1 < n:
                    maxWeight = weight[i + 1]
                i += 2
            else:
                maxWeight = max(maxWeight, weight[i])
                i += 1
        return result


weight = [2, 5, 1, 4, 3]
print(Solution().maxBalancedShipments(weight))
weight = [4, 4]
print(Solution().maxBalancedShipments(weight))
weight = [1, 2, 3, 1]
print(Solution().maxBalancedShipments(weight))
weight = [5, 4, 3, 2, 1]
print(Solution().maxBalancedShipments(weight))
