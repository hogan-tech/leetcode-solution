from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        result = float('inf')
        for i in range(1, len(nums)):
            prefix[i] = min(prefix[i - 1], nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = min(suffix[i], nums[i - 1])
        
        for i in range(len(nums)):
            if prefix[i] < nums[i] and nums[i] > suffix[i]:
                result = min(result, nums[i] + prefix[i] + suffix[i])
        return result if result != float('inf') else -1

'''
[5, 4, 4, 4, 4, 2]

[5, 4, 8, 7, 10, 2]

[2, 2, 2, 2, 2, 2]
'''
nums = [8, 6, 1, 5, 3]
print(Solution().minimumSum(nums))
nums = [5, 4, 8, 7, 10, 2]
print(Solution().minimumSum(nums))
nums = [6, 5, 4, 3, 4, 5]
print(Solution().minimumSum(nums))
