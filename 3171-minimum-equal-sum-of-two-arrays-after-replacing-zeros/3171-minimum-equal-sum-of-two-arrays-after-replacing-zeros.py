# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = 0
        zero1 = zero2 = 0

        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zero1 += 1

        for i in nums2:
            sum2 += i
            if i == 0:
                sum2 += 1
                zero2 += 1

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)


'''
nums1 = 6 -> 0:2
nums2 = 11 -> 0:1

nums1 = 4 -> 0:2
nums2 = 5 -> 0:0
'''
nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
print(Solution().minSum(nums1, nums2))
nums1 = [2, 0, 2, 0]
nums2 = [1, 4]
print(Solution().minSum(nums1, nums2))
nums1
