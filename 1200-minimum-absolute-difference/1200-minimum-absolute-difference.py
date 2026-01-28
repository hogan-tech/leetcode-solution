# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []

        minDiff = float('inf')

        for i in range(len(arr) - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minDiff:
                result.append([arr[i], arr[i + 1]])
        return result


arr = [4, 2, 1, 3]
print(Solution().minimumAbsDifference(arr))
arr = [1, 3, 6, 10, 15]
print(Solution().minimumAbsDifference(arr))
arr = [3, 8, -10, 23, 19, -4, -14, 27]
print(Solution().minimumAbsDifference(arr))
