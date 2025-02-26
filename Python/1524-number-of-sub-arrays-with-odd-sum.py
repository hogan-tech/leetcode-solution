# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = 0
        oddCount = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            prefixSum += num
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % MOD


arr = [1, 3, 5]
print(Solution().numOfSubarrays(arr))
arr = [2, 4, 6]
print(Solution().numOfSubarrays(arr))
arr = [1, 2, 3, 4, 5, 6, 7]
print(Solution().numOfSubarrays(arr))
