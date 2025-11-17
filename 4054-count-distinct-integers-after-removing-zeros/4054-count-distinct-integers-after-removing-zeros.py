# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        L = len(s)

        total = 0
        for length in range(1, L):
            total += 9 ** length

        dp = [[0] * 2 for _ in range(L + 1)]

        dp[L][0] = 1
        dp[L][1] = 1

        for i in range(L - 1, -1, -1):
            limit = int(s[i])
            for tight in (0, 1):
                maxDigit = limit if tight else 9
                result = 0
                for dig in range(1, maxDigit + 1):
                    newTight = tight and (dig == maxDigit)
                    result += dp[i + 1][newTight]
                dp[i][tight] = result

        total += dp[0][1]
        return total


n = 10
print(Solution().countDistinct(n))
n = 3
print(Solution().countDistinct(n))
