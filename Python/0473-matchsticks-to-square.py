# time complexity: O(4^n)
# space complexity: O(n)
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        paremiter = sum(matchsticks)
        side = paremiter // 4
        if side * 4 != paremiter:
            return False
        sums = [0 for _ in range(4)]
        matchsticks.sort(reverse=True)
        def backtrack(idx: int):
            if idx == n:
                return sums[0] == sums[1] == sums[2] == side
            for i in range(4):
                if sums[i] + matchsticks[idx] <= side:
                    sums[i] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sums[i] -= matchsticks[idx]
            return False
        return backtrack(0)


matchsticks = [1, 1, 2, 2, 2]
print(Solution().makesquare(matchsticks))
matchsticks = [3, 3, 3, 3, 4]
print(Solution().makesquare(matchsticks))
