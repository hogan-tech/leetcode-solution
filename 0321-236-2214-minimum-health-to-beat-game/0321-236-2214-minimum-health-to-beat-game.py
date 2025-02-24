# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage = 0
        totalDamage = 0
        for i in range(len(damage)):
            totalDamage += damage[i]
            maxDamage = max(maxDamage, damage[i])

        return sum(damage) - min(armor, maxDamage) + 1


damage = [2, 7, 4, 3]
armor = 4
print(Solution().minimumHealth(damage, armor))
damage = [2, 5, 3, 4]
armor = 7
print(Solution().minimumHealth(damage, armor))
damage = [3, 3, 3]
armor = 0
print(Solution().minimumHealth(damage, armor))
damage = [3]
armor = 1
print(Solution().minimumHealth(damage, armor))
