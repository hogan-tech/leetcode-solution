# time complexity: O(n^(t/m) + 1)
# space complexity: O(t/m)
from typing import List

# Backtrack
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, comb: List[int], remain: int):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    comb.append(candidates[i])
                    backtrack(i, comb, remain - candidates[i])
                    comb.pop()
        backtrack(0, [], target)
        return result

# time complexity: O(t*n*s^2log(s))
# space complexity: O(t*n*c)
# Bottom Up
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if nums[j] <= i:
                    for prev in dp[i - nums[j]]:
                        temp = prev + [nums[j]]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target]


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))
candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))
