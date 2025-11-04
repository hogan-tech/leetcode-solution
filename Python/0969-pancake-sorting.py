# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]):
        result = []
        for lastIdx in range(len(arr), 1, -1):
            currIdx = arr.index(lastIdx)
            result.extend([currIdx + 1, lastIdx])
            arr = arr[:currIdx:-1] + arr[:currIdx]
        return result


arr = [3, 2, 4, 1]
print(Solution().pancakeSort(arr))
arr = [1, 2, 3]
print(Solution().pancakeSort(arr))
