# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        numQueue = deque(nums)
        while len(numQueue) > 0:
            if len(set(numQueue)) == len(numQueue):
                return count
            for _ in range(min(3, len(numQueue))):
                numQueue.popleft()
            count += 1

        return count


nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
print(Solution().minimumOperations(nums))
nums = [4, 5, 6, 4, 4]
print(Solution().minimumOperations(nums))
nums = [6, 7, 8, 9]
print(Solution().minimumOperations(nums))
nums = [2]
print(Solution().minimumOperations(nums))
nums = [5, 5]
print(Solution().minimumOperations(nums))
