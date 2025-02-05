# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[i - 1] + arr[i])
        prefix.insert(0, 0)
        count = 0
        for i in range(k, len(prefix)):
            tempSum = prefix[i] - prefix[i - k]
            if tempSum >= target:
                count += 1
        return count


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(Solution().numOfSubarrays(arr, k, threshold))
arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(Solution().numOfSubarrays(arr, k, threshold))
