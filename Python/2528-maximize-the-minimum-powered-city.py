# time complexity: O(nlogD)
# space complexity: O(n)
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        count = [0] * (n + 1)

        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            count[left] += stations[i]
            count[right] -= stations[i]

        def check(val: int) -> bool:
            diff = count.copy()
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True

        leftIdx, rightIdx = min(stations), sum(stations) + k
        result = 0
        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            if check(midIdx):
                result = midIdx
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1
        return result


stations = [1, 2, 4, 5, 0]
r = 1
k = 2
print(Solution().maxPower(stations, r, k))
stations = [4, 4, 4, 4]
r = 0
k = 3
print(Solution().maxPower(stations, r, k))
