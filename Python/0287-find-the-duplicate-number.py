# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(nums))
