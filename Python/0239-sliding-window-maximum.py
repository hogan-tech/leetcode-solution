# time complexity: O(n)
# space complexity: O(ns)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def cleanUp(i: int, currWindow: deque, nums: List[int]):
            while currWindow and nums[i] >= nums[currWindow[-1]]:
                currWindow.pop()

        if len(nums) == 1:
            return nums
        result = []
        currWindow = deque()
        for i in range(k):
            cleanUp(i, currWindow, nums)
            currWindow.append(i)

        result.append(nums[currWindow[0]])
        for i in range(k, len(nums)):
            cleanUp(i, currWindow, nums)
            if currWindow and currWindow[0] <= (i - k):
                currWindow.popleft()
            currWindow.append(i)
            result.append(nums[currWindow[0]])
        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
nums = [1]
k = 1
print(Solution().maxSlidingWindow(nums, k))
