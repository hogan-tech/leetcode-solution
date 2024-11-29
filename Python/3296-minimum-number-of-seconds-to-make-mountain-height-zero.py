# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def maxHeightReduced(worker_time, T):
            low, high = 0, mountainHeight
            while low < high:
                mid = (low + high + 1) // 2
                if worker_time * mid * (mid + 1) // 2 <= T:
                    low = mid
                else:
                    high = mid - 1
            return low

        low, high = 0, max(workerTimes) * mountainHeight * \
            (mountainHeight + 1) // 2

        while low < high:
            mid = (low + high) // 2
            totalHeightReduced = 0

            for workerTime in workerTimes:
                totalHeightReduced += maxHeightReduced(workerTime, mid)

            if totalHeightReduced >= mountainHeight:
                high = mid
            else:
                low = mid + 1

        return low


mountainHeight = 4
workerTimes = [2, 1, 1]
print(Solution().minNumberOfSeconds(mountainHeight, workerTimes))
