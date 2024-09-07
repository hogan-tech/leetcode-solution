# time complexity: O(n*logs)
# space complexity: O(1)
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight, totalWeight = -1, 0
        for weight in weights:
            maxWeight = max(maxWeight, weight)
            totalWeight += maxWeight
        left, right = maxWeight, totalWeight
        while left < right:
            mid = left + (right - left) // 2
            daysNeeded, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight
            if daysNeeded > days:
                left = mid + 1
            else:
                right = mid
        return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(Solution().shipWithinDays(weights, days))
