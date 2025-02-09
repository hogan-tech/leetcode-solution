# time complexity: O(n!)
# space complexity: O(n)
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0

        def backtrack(comb):
            nonlocal count
            if len(comb) == 2:
                if nums[comb[0]] + nums[comb[1]] == target:
                    count += 1
                return

            for i in range(len(nums)):
                if i not in comb:
                    comb.append(i)
                    backtrack(comb)
                    comb.pop()

        backtrack([])
        return count


nums = ["777", "7", "77", "77"]
target = "7777"
print(Solution().numOfPairs(nums, target))
nums = ["123", "4", "12", "34"]
target = "1234"
print(Solution().numOfPairs(nums, target))
nums = ["1", "1", "1"]
target = "11"
print(Solution().numOfPairs(nums, target))
