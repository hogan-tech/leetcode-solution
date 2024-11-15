# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        result = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            result = min(result, right - left - 1)
            left += 1
        return result


arr = [1, 2, 3, 10, 4, 2, 3, 5]
print(Solution().findLengthOfShortestSubarray(arr))
