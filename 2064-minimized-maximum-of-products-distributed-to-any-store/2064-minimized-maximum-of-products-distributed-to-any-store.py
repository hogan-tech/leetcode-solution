# time complexity: O(m+(n-m)logm)
# space complexity: O(m)
from heapq import heapify, heappop, heappush
import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        typeStorePairs = []
        for quantity in quantities:
            typeStorePairs.append((-quantity, quantity, 1))
        heapify(typeStorePairs)
        for i in range(n - len(quantities)):
            (negRatio, totalQuantityType, storesAssignedType) = heappop(typeStorePairs)
            newStoreAssignedType = storesAssignedType + 1
            newRatio = totalQuantityType / newStoreAssignedType
            heappush(typeStorePairs, (-newRatio,
                     totalQuantityType, newStoreAssignedType))
        _, totalQuantityType, storesAssignedType = heappop(typeStorePairs)
        return math.ceil(totalQuantityType/storesAssignedType)


n = 6
quantities = [11, 6]
print(Solution().minimizedMaximum(n, quantities))
n = 7
quantities = [15, 10, 10]
print(Solution().minimizedMaximum(n, quantities))
n = 1
quantities = [100000]
print(Solution().minimizedMaximum(n, quantities))
