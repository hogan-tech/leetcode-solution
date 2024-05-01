from typing import List


class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        difference = [nums1[i] - nums2[i] for i in range(len(nums1))]
        difference.sort()

        left, right = 0, len(nums1) - 1
        while left < right:
            if difference[left] + difference[right] > 0:
                result += right - left
                right -= 1
            else:
                left += 1
        return result


nums1 = [1, 10, 6, 2]
nums2 = [1, 4, 1, 5]

print(Solution().countPairs(nums1, nums2))
