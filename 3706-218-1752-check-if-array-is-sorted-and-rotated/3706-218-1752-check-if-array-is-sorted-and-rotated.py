# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sortedNums = sorted(nums)
        newArray = nums[:] + nums[:]
        for i in range(n):
            if newArray[i: i + n] == sortedNums:
                return True
        return False


nums = [3, 4, 5, 1, 2]
print(Solution().check(nums))
nums = [2, 1, 3, 4]
print(Solution().check(nums))
nums = [1, 2, 3]
print(Solution().check(nums))
