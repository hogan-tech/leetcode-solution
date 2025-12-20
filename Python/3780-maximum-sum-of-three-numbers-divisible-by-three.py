# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        groups = {0: [], 1: [], 2: []}
        for num in nums:
            groups[num % 3].append(num)

        for group in groups:
            groups[group].sort(reverse=True)

        result = 0

        if len(groups[0]) >= 3:
            result = max(result, sum(groups[0][:3]))

        if len(groups[1]) >= 3:
            result = max(result, sum(groups[1][:3]))

        if len(groups[2]) >= 3:
            result = max(result, sum(groups[2][:3]))

        if groups[0] and groups[1] and groups[2]:
            result = max(result, groups[0][0] + groups[1][0] + groups[2][0])

        return result


nums = [4, 2, 3, 1]
print(Solution().maximumSum(nums))
nums = [2, 1, 5]
print(Solution().maximumSum(nums))
