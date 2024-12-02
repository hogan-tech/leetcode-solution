# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == 2 * arr[j]:
                    return True
        return False


arr = [10, 2, 5, 3]
print(Solution().checkIfExist(arr))
arr = [3, 1, 7, 11]
print(Solution().checkIfExist(arr))
arr = [7, 1, 14, 11]
print(Solution().checkIfExist(arr))
