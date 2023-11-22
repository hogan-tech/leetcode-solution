# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        ans = []
        curr = 0
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1
        return ans


nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(nums))
