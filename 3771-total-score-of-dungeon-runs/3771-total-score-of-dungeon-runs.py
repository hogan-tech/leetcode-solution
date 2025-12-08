# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
import bisect


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + damage[i - 1]
        total = 0
        for i in range(1, n + 1):
            need = prefix[i] - (hp - requirement[i - 1])
            k = bisect.bisect_left(prefix, need)
            if k <= i - 1:
                total += (i - k)
        return total


hp = 11
damage = [3, 6, 7]
requirement = [4, 2, 5]
print(Solution().totalScore(hp, damage, requirement))
hp = 2
damage = [10000, 1]
requirement = [1, 1]
print(Solution().totalScore(hp, damage, requirement))
