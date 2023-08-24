from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeList = sorted(nums1 + nums2)
        mergeListLen = len(mergeList)
        mid = mergeListLen//2
        if mergeListLen % 2:
            return float(mergeList[mid])
        else:
            return (mergeList[mid] + mergeList[mid-1])/2


nums1 = [1, 3]
nums2 = [2, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
