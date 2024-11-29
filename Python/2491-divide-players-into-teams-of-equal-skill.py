# time complexity: O(nlogn)
# space complexity: O(s)
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result = 0
        totalSkill = sum(skill) * 2 // len(skill)
        for i in range(len(skill) // 2):
            if skill[i] + skill[len(skill) - i - 1] == totalSkill:
                result += skill[i] * skill[len(skill) - i - 1]
            else:
                return -1
        return result


skill = [1, 1, 2, 3]
print(Solution().dividePlayers(skill))
