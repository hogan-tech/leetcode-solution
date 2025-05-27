# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def greedy(nums, smallFirst=True):
            if n <= 1:
                return 0
            ans = 0
            for i in range(n-1):
                if smallFirst and nums[i] >= nums[i+1]:
                    ans += nums[i] - (nums[i+1]-1)
                    nums[i] = nums[i+1] - 1
                elif not smallFirst and nums[i] <= nums[i+1]:
                    ans += nums[i+1] - (nums[i]-1)
                    nums[i+1] = nums[i] - 1
                smallFirst = not smallFirst
            return ans
        n = len(nums)
        return min(greedy(nums[:], True), greedy(nums[:], False))


nums = [1, 2, 3]
print(Solution().movesToMakeZigzag(nums))
nums = [9, 6, 1, 6, 2]
print(Solution().movesToMakeZigzag(nums))
