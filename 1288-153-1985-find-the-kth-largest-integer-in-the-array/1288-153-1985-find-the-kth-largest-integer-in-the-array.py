# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        return str(nums[-k])


nums = ["3", "6", "7", "10"]
k = 4
print(Solution().kthLargestNumber(nums, k))
nums = ["2", "21", "12", "1"]
k = 3
print(Solution().kthLargestNumber(nums, k))
nums = ["0", "0"]
k = 2
print(Solution().kthLargestNumber(nums, k))
