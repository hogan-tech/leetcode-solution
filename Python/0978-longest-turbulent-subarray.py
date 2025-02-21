# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 0
        n = len(arr)
        if n == 1:
            return 1

        result = 1
        while right < n:
            while left < n - 1 and arr[left] == arr[left + 1]:
                left += 1
            while right < n - 1 and (arr[right - 1] > arr[right] < arr[right + 1] or arr[right - 1] < arr[right] > arr[right + 1]):
                right += 1
            result = max(result, right - left + 1)
            left = right
            right += 1
        return result


arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(Solution().maxTurbulenceSize(arr))
arr = [4, 8, 12, 16]
print(Solution().maxTurbulenceSize(arr))
arr = [100]
print(Solution().maxTurbulenceSize(arr))
