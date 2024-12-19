# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        prefixSum = arr[:]
        suffixSum = arr[:]
        for i in range(1, n):
            prefixSum[i] = max(prefixSum[i-1], prefixSum[i])
        for i in range(n - 2, -1, -1):
            suffixSum[i] = min(suffixSum[i+1], suffixSum[i])

        result = 0
        for i in range(n):
            if i == 0 or suffixSum[i] > prefixSum[i-1]:
                result += 1
        return result


arr = [4, 3, 2, 1, 0]
print(Solution().maxChunksToSorted(arr))
arr = [1, 0, 2, 3, 4]
print(Solution().maxChunksToSorted(arr))
