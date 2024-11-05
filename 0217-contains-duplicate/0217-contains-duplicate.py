# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


Input = [1, 2, 3]

print(Solution().containsDuplicate(Input))
