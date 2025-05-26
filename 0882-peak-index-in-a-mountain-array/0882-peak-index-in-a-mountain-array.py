from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid] > arr[mid + 1]:
                right = mid
        return left


arr = [0, 10, 5, 2]
print(Solution().peakIndexInMountainArray(arr))
arr = [0, 2, 1, 0]
print(Solution().peakIndexInMountainArray(arr))
arr = [0, 10, 5, 2]
print(Solution().peakIndexInMountainArray(arr))
