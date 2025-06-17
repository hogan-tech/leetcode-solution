# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], dp[left] + 1)
        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)


nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))
nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))
nums = [7, 7, 7, 7, 7, 7, 7]
print(Solution().lengthOfLIS(nums))
