# time complexity: O(nlogw)
# space complexity: O(1)
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= k

        left, right = 0, 10**8
        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if possible(mid):
                right = mid
            else:
                left = mid
        return left


stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
print(Solution().minmaxGasDist(stations, k))
stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98]
k = 1
print(Solution().minmaxGasDist(stations, k))
