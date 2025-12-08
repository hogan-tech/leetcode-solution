# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        result = 0
        for num1, num2 in zip(nums1, nums2):
            result += num1 * num2
        return result


nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
print(Solution().minProductSum(nums1, nums2))
nums1 = [2, 1, 4, 5, 7]
nums2 = [3, 2, 4, 8, 6]
print(Solution().minProductSum(nums1, nums2))
