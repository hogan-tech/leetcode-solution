# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        result = -1
        for key, value in freq.items():
            if key == value:
                result = max(result, key)
        return result


arr = [2, 2, 3, 4]
print(Solution().findLucky(arr))
arr = [1, 2, 2, 3, 3, 3]
print(Solution().findLucky(arr))
arr = [2, 2, 2, 3, 3]
print(Solution().findLucky(arr))
