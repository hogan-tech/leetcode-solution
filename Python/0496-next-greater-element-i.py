# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greaterDict = defaultdict(int)

        for num in nums2:
            while stack and num > stack[-1]:
                greaterDict[stack.pop()] = num
            stack.append(num)

        while stack:
            greaterDict[stack.pop()] = -1
            
        result = []
        for num in nums1:
            result.append(greaterDict[num])
        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(Solution().nextGreaterElement(nums1, nums2))
