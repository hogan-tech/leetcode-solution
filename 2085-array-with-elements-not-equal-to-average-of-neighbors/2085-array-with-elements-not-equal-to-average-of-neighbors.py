# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        midIdx = len(nums) // 2
        smallNums = nums[:midIdx]
        largeNums = nums[midIdx:]
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            result[i] = smallNums.pop() if i % 2 else largeNums.pop()
        return result


nums = [1, 2, 3, 4, 5]
print(Solution().rearrangeArray(nums))
nums = [6, 2, 0, 9, 7]
print(Solution().rearrangeArray(nums))
