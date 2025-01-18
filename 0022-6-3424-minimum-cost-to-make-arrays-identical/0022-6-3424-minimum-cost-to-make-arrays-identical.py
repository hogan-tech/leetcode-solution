# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        if arr == brr:
            return 0

        result1 = sum(abs(arr[i] - brr[i]) for i in range(len(arr)))
        arr.sort()
        brr.sort()
        result2 = sum(abs(arr[i] - brr[i]) for i in range(len(arr)))

        return min(result1, result2 + k)


arr = [-7, 9, 5]
brr = [7, -2, -5]
k = 2
print(Solution().minCost(arr, brr, k))
arr = [2, 1]
brr = [2, 1]
k = 0
print(Solution().minCost(arr, brr, k))
