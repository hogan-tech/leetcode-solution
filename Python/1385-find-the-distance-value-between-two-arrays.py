# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        result = 0
        for i in range(len(arr1)):
            left = 0
            right = len(arr2) - 1
            valid = True
            while left <= right:
                mid = left + (right - left) // 2
                if arr2[mid] == arr1[i]:
                    valid = False
                    break
                elif arr2[mid] < arr1[i]:
                    left = mid + 1
                else:
                    right = mid - 1

            if left < len(arr2) and abs(arr2[left] - arr1[i]) <= d:
                valid = False
            if right >= 0 and abs(arr2[right] - arr1[i]) <= d:
                valid = False
            if valid:
                result += 1
        return result


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(Solution().findTheDistanceValue(arr1, arr2, d))
arr1 = [1, 4, 2, 3]
arr2 = [-4, -3, 6, 10, 20, 30]
d = 3
print(Solution().findTheDistanceValue(arr1, arr2, d))
arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6
print(Solution().findTheDistanceValue(arr1, arr2, d))
