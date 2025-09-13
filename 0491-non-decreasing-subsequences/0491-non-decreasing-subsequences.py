# time complexity: O(n * 2^n)
# space complexity: O(n * 2^n)
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        combSet = set()

        def backtrack(start, comb):
            if len(comb) >= 2:
                combSet.add(tuple(comb))
            for i in range(start, len(nums)):
                if not comb or nums[i] >= comb[-1]:
                    comb.append(nums[i])
                    backtrack(i + 1, comb)
                    comb.pop()
        backtrack(0, [])
        return [list(comb) for comb in combSet]


nums = [4, 6, 7, 7]
print(Solution().findSubsequences(nums))
nums = [4, 4, 3, 2, 1]
print(Solution().findSubsequences(nums))
