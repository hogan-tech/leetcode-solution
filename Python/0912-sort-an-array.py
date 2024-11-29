# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, aList: List[int], bList: List[int]):
        sortedArray = []
        left = 0
        right = 0
        while left < len(aList) and right < len(bList):
            if aList[left] < bList[right]:
                sortedArray.append(aList[left])
                left += 1
            else:
                sortedArray.append(bList[right])
                right += 1
        sortedArray += aList[left:]
        sortedArray += bList[right:]
        return sortedArray


nums = [5, 2, 3, 1]
print(Solution().sortArray(nums))
