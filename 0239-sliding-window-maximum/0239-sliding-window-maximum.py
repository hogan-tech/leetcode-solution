from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = []
        for i in range(n):
            while queue and queue[-1] <= i - k:
                queue.pop()
            if queue and nums[queue[-1]] > nums[i]:
                while queue and nums[queue[0]] < nums[i]:
                    queue.popleft()
                queue.appendleft(i)
            else:
                queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[-1]])
        return res
        # maxList = []
        # for i in range(len(nums) - k + 1):
        #     maxList.append(max(nums[i:i+k]))
        # return maxList


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
