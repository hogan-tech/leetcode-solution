# time complexity: O(nlogn + nlogv)
# space complexity: O(n)
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        def checkValidPairs(diff: int):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= diff:
                    count += 1
                    i += 1
                i += 1
            return count
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (right + left) // 2
            if checkValidPairs(mid) < p:
                left = mid + 1
            else:
                right = mid
        return left


'''
1, 1, 2, 3, 7, 10

diff -> 10 - 1 = 9

mid = 9 // 2 = 4

check if diff between 4 pairs >= p then change mid

'''
nums = [10, 1, 2, 7, 1, 3]
p = 2
print(Solution().minimizeMax(nums, p))
nums = [4, 2, 1, 2]
p = 1
print(Solution().minimizeMax(nums, p))
