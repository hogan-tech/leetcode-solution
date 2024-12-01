# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        numSet = set(nums)
        outLier = float('-inf')

        for num in nums:
            remainingSum = total - num
            if remainingSum % 2 == 0:
                specialSum = remainingSum // 2
                if specialSum in numSet:
                    if specialSum == num and count[num] < 2:
                        continue
                    outLier = max(outLier, num)
        return outLier


nums = [2, 3, 5, 10]
print(Solution().getLargestOutlier(nums))
nums = [-2, -1, -3, -6, 4]
print(Solution().getLargestOutlier(nums))
nums = [1, 1, 1, 1, 1, 5, 5]
print(Solution().getLargestOutlier(nums))
nums = [874, 159, -838, -375, 658]
print(Solution().getLargestOutlier(nums))
nums = [958, 777, -746, 566, 989]
print(Solution().getLargestOutlier(nums))
