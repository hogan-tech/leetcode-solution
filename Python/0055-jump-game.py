# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
    
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        GOOD = 1
        BAD = 0
        UNKNOWN = -1
        dp = [UNKNOWN for _ in range(len(nums))]
        dp[-1] = GOOD
        for i in range(len(nums) - 2, -1, -1):
            lastPos = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, lastPos + 1):
                if dp[j] == GOOD:
                    dp[i] = GOOD
                    break
        return dp[0] == GOOD


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
