from typing import List


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        n = len(blocks)
        blocks.sort(reverse=True)

        dp = [[-1] * (n+1) for _ in range(n)]

        def solve(b, w):
            if b == n:
                return 0
            if w == 0:
                return float('inf')
            if w >= n-b:
                return blocks[b]
            if dp[b][w] != -1:
                return dp[b][w]
            workHere = max(blocks[b], solve(b+1, w - 1))
            splitHere = split + solve(b, min(2*w, n-b))
            dp[b][w] = min(workHere, splitHere)
            return dp[b][w]
        return solve(0, 1)


blocks = [1]
split = 1


print(Solution().minBuildTime(blocks, split))
