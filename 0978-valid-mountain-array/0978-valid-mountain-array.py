# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1


arr = [2, 1]
print(Solution().validMountainArray(arr))
arr = [3, 5, 5]
print(Solution().validMountainArray(arr))
arr = [0, 3, 2, 1]
print(Solution().validMountainArray(arr))
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().validMountainArray(arr))
