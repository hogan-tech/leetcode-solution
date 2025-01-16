# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)

        freq = {}

        for num in nums1:
            freq[num] = freq.get(num, 0) + len2

        for num in nums2:
            freq[num] = freq.get(num, 0) + len1

        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num

        return ans


nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
print(Solution().xorAllNums(nums1, nums2))
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().xorAllNums(nums1, nums2))
