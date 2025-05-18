# time complexity: O(nlogn)
# space complexity: O(1)
from bisect import bisect_left
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        nums2.reverse()
        result = 0
        for i, num in enumerate(nums1):
            leftIdx = bisect_left(nums2, num)
            result = max(result, len(nums2) - leftIdx - 1 - i)
        return result


nums1 = [55, 30, 5, 4, 2]
nums2 = [100, 20, 10, 10, 5]
print(Solution().maxDistance(nums1, nums2))
nums1 = [2, 2, 2]
nums2 = [10, 10, 1]
print(Solution().maxDistance(nums1, nums2))
nums1 = [30, 29, 19, 5]
nums2 = [25, 25, 25, 25, 25]
print(Solution().maxDistance(nums1, nums2))
