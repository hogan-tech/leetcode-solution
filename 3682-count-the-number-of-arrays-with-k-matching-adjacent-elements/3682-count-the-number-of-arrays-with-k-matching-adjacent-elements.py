# time complexity: O(log(n - m))
# space complexity: O(1)
MOD = 10**9 + 7
MX = 10**5

fact = [0] * MX
invFact = [0] * MX


def qpow(x, n):
    result = 1
    while n:
        if n & 1:
            result = result * x % MOD
        x = x * x % MOD
        n >>= 1
    return result


def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    invFact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    for i in range(MX - 1, 0, -1):
        invFact[i - 1] = invFact[i] * i % MOD


def comb(n, m):
    return fact[n] * invFact[m] % MOD * invFact[n - m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD


n = 3
m = 2
k = 1
print(Solution().countGoodArrays(n, m, k))
n = 4
m = 2
k = 2
print(Solution().countGoodArrays(n, m, k))
n = 5
m = 2
k = 0
print(Solution().countGoodArrays(n, m, k))
