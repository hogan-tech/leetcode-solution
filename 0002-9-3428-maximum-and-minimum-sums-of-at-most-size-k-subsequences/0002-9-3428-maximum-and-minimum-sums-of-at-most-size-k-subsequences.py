# time complexity: O(nlogn + nk) = O(n^2)
# space complexity: O(nk)
from typing import List

MOD = 10**9 + 7


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        def modInv(x, mod=MOD):
            return pow(x, mod-2, mod)

        def precomputeFactorials(n, mod=MOD):
            fact = [1] * (n + 1)
            invFact = [1] * (n + 1)
            for i in range(2, n + 1):
                fact[i] = fact[i-1] * i % mod
            invFact[n] = modInv(fact[n], mod)
            for i in range(n-1, 0, -1):
                invFact[i] = invFact[i+1] * (i+1) % mod
            return fact, invFact

        def binomial(n, r, fact, invFact, mod=MOD):
            if n < r or r < 0:
                return 0
            return fact[n] * invFact[r] % mod * invFact[n-r] % mod

        nums.sort()
        n = len(nums)

        fact, invFact = precomputeFactorials(n)

        binomPrecompute = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            for j in range(min(i + 1, k + 1)):
                binomPrecompute[i][j] = binomial(i, j, fact, invFact)

        result = 0

        for i in range(n):
            for m in range(1, k+1):
                conMin = binomPrecompute[i][m-1] * nums[i] % MOD
                conMax = binomPrecompute[n-i-1][m-1] * nums[i] % MOD
                result = (result + conMin + conMax) % MOD

        return result


nums = [1, 2, 3]
k = 2
print(Solution().minMaxSums(nums, k))
nums = [5, 0, 6]
k = 1
print(Solution().minMaxSums(nums, k))
nums = [1, 1, 1]
k = 2
print(Solution().minMaxSums(nums, k))
nums = [1, 2, 3, 4]
k = 3
print(Solution().minMaxSums(nums, k))
