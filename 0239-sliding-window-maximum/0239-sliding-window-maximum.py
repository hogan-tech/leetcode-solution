# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monoQueue = deque()
        result = []

        left = 0
        right = 0
        while right < len(nums):
            while monoQueue and nums[monoQueue[-1]] < nums[right]:
                monoQueue.pop()
            monoQueue.append(right)
            
            if left > monoQueue[0]:
                monoQueue.popleft()
            
            if (right + 1) >= k:
                result.append(nums[monoQueue[0]])
                left += 1
            right += 1

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
nums = [1]
k = 1
print(Solution().maxSlidingWindow(nums, k))
