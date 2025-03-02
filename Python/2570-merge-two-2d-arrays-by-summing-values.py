# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        sumMap = defaultdict(int)
        result = []
        for key, value in nums1:
            sumMap[key] += value
        for key, value in nums2:
            sumMap[key] += value

        for key, value in sumMap.items():
            result.append([key, value])

        result.sort()
        return result


nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
print(Solution().mergeArrays(nums1, nums2))
nums1 = [[2, 4], [3, 6], [5, 5]]
nums2 = [[1, 3], [4, 3]]
print(Solution().mergeArrays(nums1, nums2))
