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

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(nums))
nums = [3, 1, 3, 4, 2]
print(Solution().findDuplicate(nums))
nums = [3, 3, 3, 3, 3]
print(Solution().findDuplicate(nums))
