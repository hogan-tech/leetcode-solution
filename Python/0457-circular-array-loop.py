# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def nextStep(currIdx: int, value: int, size: int):
            result = (currIdx + value) % size
            if result < 0:
                result += size
            return result

        def isNotCycle(nums, prevDirection, currIdx):
            currDirection = nums[currIdx] > 0
            if prevDirection != currDirection:
                return True
            if abs(nums[currIdx] % len(nums)) == 0:
                return True
            return False

        n = len(nums)
        for i in range(n):
            slow = fast = i
            forward = nums[i] > 0
            while True:
                slow = nextStep(slow, nums[slow], n)
                if isNotCycle(nums, forward, slow):
                    break
                fast = nextStep(fast, nums[fast], n)
                if isNotCycle(nums, forward, fast):
                    break
                fast = nextStep(fast, nums[fast], n)
                if isNotCycle(nums, forward, fast):
                    break
                if slow == fast:
                    return True
        return False


nums = [2, -1, 1, 2, 2]
print(Solution().circularArrayLoop(nums))
nums = [-1, -2, -3, -4, -5, 6]
print(Solution().circularArrayLoop(nums))
nums = [1, -1, 5, 1, 4]
print(Solution().circularArrayLoop(nums))
