# time complexity: O(n^3)
# space complexity: O(1)
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    result = max(result, (nums[i] - nums[j]) * nums[k])
        return result


nums = [12, 6, 1, 2, 7]
print(Solution().maximumTripletValue(nums))
nums = [1, 10, 3, 4, 19]
print(Solution().maximumTripletValue(nums))
nums = [1, 2, 3]
print(Solution().maximumTripletValue(nums))
nums = [10, 13, 6, 2]
print(Solution().maximumTripletValue(nums))
'''
-18
10 13 6
-6
10 13 2
14
13 6 2
'''
