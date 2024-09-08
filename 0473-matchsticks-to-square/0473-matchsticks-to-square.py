from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        Len = len(matchsticks)
        if Len == 0:
            return False
        perimeter = sum(matchsticks)
        side = perimeter // 4
        if side * 4 != perimeter:
            return False
        matchsticks.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(idx: int):
            if idx == Len:
                return sums[0] == sums[1] == sums[2] == side
            for i in range(4):
                if sums[i] + matchsticks[idx] <= side:
                    sums[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    sums[i] -= matchsticks[idx]
            return False
        return dfs(0)


matchsticks = [1, 1, 2, 2, 2]
print(Solution().makesquare(matchsticks))
