# time complexity: O(n*m^3*k)
# space complexity: O(n*m^2*k)
from typing import List


class Solution:
    def quickmul(self, x: int, y: int, mod: int) -> int:
        result, curr = 1, x % mod
        while y:
            if y & 1:
                result = result * curr % mod
            y >>= 1
            curr = curr * curr % mod
        return result

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        fac = [1] * (m + 1)
        for i in range(1, m + 1):
            fac[i] = fac[i - 1] * i % MOD

        ifac = [1] * (m + 1)
        for i in range(2, m + 1):
            ifac[i] = self.quickmul(i, MOD - 2, MOD)
        for i in range(2, m + 1):
            ifac[i] = ifac[i - 1] * ifac[i] % MOD

        numsPower = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                numsPower[i][j] = numsPower[i][j - 1] * nums[i] % MOD

        f = [
            [[[0] * (k + 1) for _ in range(m * 2 + 1)] for _ in range(m + 1)]
            for _ in range(n)
        ]

        for j in range(m + 1):
            f[0][j][j][0] = numsPower[0][j] * ifac[j] % MOD

        for i in range(n - 1):
            for j in range(m + 1):
                for p in range(m * 2 + 1):
                    for q in range(k + 1):
                        if f[i][j][p][q] == 0:
                            continue
                        q2 = (p % 2) + q
                        if q2 > k:
                            break
                        for r in range(m - j + 1):
                            p2 = (p // 2) + r
                            if p2 > m * 2:
                                continue
                            f[i + 1][j + r][p2][q2] = (
                                f[i + 1][j + r][p2][q2]
                                + f[i][j][p][q]
                                * numsPower[i + 1][r]
                                % MOD
                                * ifac[r]
                                % MOD
                            ) % MOD

        result = 0
        for p in range(m * 2 + 1):
            for q in range(k + 1):
                if bin(p).count("1") + q == k:
                    result = (result + f[n - 1][m][p][q] * fac[m] % MOD) % MOD
        return result


m = 7
k = 7
nums = [1, 10, 100, 10000, 1000000, 10000000, 100000000]
print(Solution().magicalSum(m, k, nums))
m = 2
k = 2
nums = [5, 4, 3, 2, 1]
print(Solution().magicalSum(m, k, nums))
m = 1
k = 1
nums = [28]
print(Solution().magicalSum(m, k, nums))
