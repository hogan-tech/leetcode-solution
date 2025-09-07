# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if all(x == nums[0] for x in nums):
            return 0

        target = nums[0]
        for x in nums[1:]:
            target &= x

        curr = nums[0]
        for i in range(1, n):
            curr &= nums[i]
        if curr == target:
            return 1

        result = 0
        curr = ~0
        for num in nums:
            curr &= num
            if curr == target:
                result += 1
                curr = ~0

        return result


'''
01
10
00
'''
nums = [1, 2]
print(Solution().minOperations(nums))
nums = [5, 5, 5]
print(Solution().minOperations(nums))
nums = [109, 14, 19, 32, 89]
print(Solution().minOperations(nums))
