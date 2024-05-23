# time complexity: O(n*2^n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, nums: List[int], idx: int, k: int, mp: defaultdict) -> int:
        if idx == len(nums):
            return 1
        taken = 0
        if mp[nums[idx] - k] == 0 and mp[nums[idx] + k] == 0:
            mp[nums[idx]] += 1
            taken = self.dfs(nums, idx + 1, k, mp)
            mp[nums[idx]] -= 1
        notTaken = self.dfs(nums, idx + 1, k, mp)
        return taken + notTaken

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        ans = self.dfs(nums, 0, k, mp)
        return ans - 1


nums = [2, 4, 6]
k = 2
print(Solution().beautifulSubsets(nums, k))
