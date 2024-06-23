# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        maxDeq = deque()
        minDeq = deque()
        longest = 0

        for right in range(len(nums)):
            while maxDeq and nums[maxDeq[-1]] <= nums[right]:
                maxDeq.pop()
            while minDeq and nums[minDeq[-1]] >= nums[right]:
                minDeq.pop()

            maxDeq.append(right)
            minDeq.append(right)

            while nums[maxDeq[0]] - nums[minDeq[0]] > limit:
                left += 1
                if maxDeq[0] < left:
                    maxDeq.popleft()
                if minDeq[0] < left:
                    minDeq.popleft()

            longest = max(longest, right - left + 1)

        return longest


nums = [8, 2, 4, 7]
limit = 4
print(Solution().longestSubarray(nums, limit))
