# time complexity: O((m+n)*logm)
# space complexity: O(logm)
import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        maxPotion = potions[len(potions) - 1]
        for spell in spells:
            minPotion = (success + spell - 1) // spell
            if minPotion > maxPotion:
                result.append(0)
                continue
            idx = bisect.bisect_left(potions, minPotion)
            result.append(len(potions) - idx)
        return result


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(Solution().successfulPairs(spells, potions, success))
