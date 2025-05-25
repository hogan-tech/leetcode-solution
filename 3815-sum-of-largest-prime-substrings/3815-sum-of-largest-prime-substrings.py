# time compelxity: O(n^2loglogn)
# space compelxity: O(k)
from math import isqrt


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def isPrime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, isqrt(n) + 1, 2):
                if n % i == 0:
                    return False
            return True

        primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                num = int(s[i:j])
                if isPrime(num):
                    primes.add(num)
        largestPrimes = sorted(primes, reverse=True)[:3]
        return sum(largestPrimes)


s = "12234"
print(Solution().sumOfLargestPrimes(s))
s = "111"
print(Solution().sumOfLargestPrimes(s))
