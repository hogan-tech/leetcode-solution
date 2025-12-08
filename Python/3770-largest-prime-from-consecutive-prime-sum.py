# time complexity: O(nloglogn)
# space complexity: O(n)
class Solution:
    def largestPrime(self, n: int) -> int:
        primeSet = [True] * (n + 1)
        primeSet[0] = primeSet[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primeSet[i]:
                for j in range(i*i, n+1, i):
                    primeSet[j] = False

        primes = [i for i in range(2, n+1) if primeSet[i]]

        prefixSum = 0
        result = 0
        for p in primes:
            prefixSum += p
            if prefixSum > n:
                break
            if primeSet[prefixSum]:
                result = prefixSum

        return result


n = 20
print(Solution().largestPrime(n))
n = 2
print(Solution().largestPrime(n))
