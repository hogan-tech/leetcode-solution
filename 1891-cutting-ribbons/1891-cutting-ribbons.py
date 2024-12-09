# time complexity: O(nlogm)
# space complexity: O(1)
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def isValid(mid: int, ribbons: List[int], k: int):
            count = 0
            for ribbon in ribbons:
                count += ribbon // mid
                if count >= k:
                    return True
            return False
        left = 0
        right = max(ribbons)
        while left < right:
            mid = (left + right + 1) // 2
            if isValid(mid, ribbons, k):
                left = mid
            else:
                right = mid - 1
        return left


ribbons = [9, 7, 5]
k = 3
print(Solution().maxLength(ribbons, k))
ribbons = [7, 5, 9]
k = 4
print(Solution().maxLength(ribbons, k))
ribbons = [5, 7, 9]
k = 22
print(Solution().maxLength(ribbons, k))
