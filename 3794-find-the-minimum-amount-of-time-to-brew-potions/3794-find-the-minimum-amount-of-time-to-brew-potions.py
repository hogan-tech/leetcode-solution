# time complexity: O(m*n)
# space complexity: O(m)
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        skillLen = len(skill)
        manaLen = len(mana)
        dp = [0 for _ in range(skillLen)]
        for manaIdx in range(manaLen):
            currTime = 0
            for skillIdx in range(skillLen):
                currTime = max(currTime, dp[skillIdx]) + skill[skillIdx] * mana[manaIdx]
            dp[-1] = currTime
            for skillIdx in range(skillLen - 2, -1, -1):
                dp[skillIdx] = dp[skillIdx + 1] - skill[skillIdx + 1] * mana[manaIdx]
        return dp[-1]


skill = [1, 5, 2, 4]
mana = [5, 1, 4, 2]
print(Solution().minTime(skill, mana))
skill = [1, 1, 1]
mana = [1, 1, 1]
print(Solution().minTime(skill, mana))
skill = [1, 2, 3, 4]
mana = [1, 2]
print(Solution().minTime(skill, mana))
