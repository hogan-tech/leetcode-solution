# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        for i in range(1, len(target)):
            result += max(target[i] - target[i - 1], 0)
        return result


target = [1, 2, 3, 2, 1]
print(Solution().minNumberOperations(target))
target = [3, 1, 1, 2]
print(Solution().minNumberOperations(target))
target = [3, 1, 5, 4, 2]
print(Solution().minNumberOperations(target))
