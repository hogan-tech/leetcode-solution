# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1
        return ans


arr = [2, 2, 1, 2, 1]
print(Solution().maximumElementAfterDecrementingAndRearranging(arr))
