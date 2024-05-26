# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def eligibleComb(n, totalAbsences, consecutiveLates):
            if totalAbsences >= 2 or consecutiveLates >= 3:
                return 0
            if n == 0:
                return 1
            if memo[n][totalAbsences][consecutiveLates] != -1:
                return memo[n][totalAbsences][consecutiveLates]

            count = eligibleComb(n - 1, totalAbsences, 0)
            count = (
                count +
                eligibleComb(n - 1, totalAbsences + 1, 0)
            ) % MOD
            count = (
                count +
                eligibleComb(n - 1,
                             totalAbsences,
                             consecutiveLates + 1)
            ) % MOD

            memo[n][totalAbsences][consecutiveLates] = count
            return count
        return eligibleComb(n, 0, 0)


n = 2
print(Solution().checkRecord(n))
