# time complexity: O(log(min(m, n)))
# space complexity: O(1)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2

        def binaryCut(targetIdx, aStart, aEnd, bStart, bEnd):
            if aStart > aEnd:
                return nums2[targetIdx - aStart]
            if bStart > bEnd:
                return nums1[targetIdx - bStart]

            aMid, bMid = (aStart + aEnd) // 2, (bStart + bEnd) // 2
            aVal, bVal = nums1[aMid], nums2[bMid]

            if aMid + bMid < targetIdx:
                if aVal > bVal:
                    return binaryCut(targetIdx, aStart, aEnd, bMid + 1, bEnd)
                else:
                    return binaryCut(targetIdx, aMid + 1, aEnd, bStart, bEnd)
            else:
                if aVal > bVal:
                    return binaryCut(targetIdx, aStart, aMid - 1, bStart, bEnd)
                else:
                    return binaryCut(targetIdx, aStart, aEnd, bStart, bMid - 1)

        if n % 2:
            return binaryCut(n // 2, 0, n1 - 1, 0, n2 - 1)
        else:
            return (binaryCut(n // 2 - 1, 0, n1 - 1, 0, n2 - 1) + binaryCut(n // 2, 0, n1 - 1, 0, n2 - 1)) / 2

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0

        def getMin():
            nonlocal idx1, idx2
            if idx1 < n1 and idx2 < n2:
                if nums1[idx1] < nums2[idx2]:
                    ans = nums1[idx1]
                    idx1 += 1
                else:
                    ans = nums2[idx2]
                    idx2 += 1
            elif idx2 == n2:
                ans = nums1[idx1]
                idx1 += 1
            else:
                ans = nums2[idx2]
                idx2 += 1
            return ans

        total = n1 + n2
        mid = total // 2

        if total % 2 == 0:
            for _ in range(mid - 1):
                getMin()
            first = getMin()
            second = getMin()
            return (first + second) / 2
        else:
            for _ in range(mid):
                getMin()
            return getMin()


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = [1, 3]
nums2 = [2, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
