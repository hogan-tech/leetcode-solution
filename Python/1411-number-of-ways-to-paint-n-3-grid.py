# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        x, y = 6, 6

        for _ in range(2, n + 1):
            nexX = (3 * x + 2 * y) % MOD
            newY = (2 * x + 2 * y) % MOD
            x, y = nexX, newY

        return (x + y) % MOD


n = 1
print(Solution().numOfWays(n))
n = 5000
print(Solution().numOfWays(n))
