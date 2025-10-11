# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        strength = {k: k*count[k] for k in count}
        spells = [0, 0, 0] + sorted(list(strength.keys()))
        n = len(spells)
        dp = [0 for _ in range(n)]
        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])

        return dp[-1]


power = [1, 1, 3, 4]
print(Solution().maximumTotalDamage(power))
power = [7, 1, 6, 6]
print(Solution().maximumTotalDamage(power))
