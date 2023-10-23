from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]


arr = [1, 2, 3, 4, 5]
k = 3
x = 4


print(Solution().findClosestElements(arr, k, x))
