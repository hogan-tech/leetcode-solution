# time complexity: O(rlog(log(r)) + r - l)
# space complexity: O(r)
from typing import List


class Solution:
    def seive(self, upperBound):
        sieve = [True] * (upperBound + 1)
        sieve[0] = sieve[1] = False
        for number in range(2, int(upperBound ** 0.5) + 1):
            if sieve[number]:
                for multiple in range(number * number, upperBound + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieveArr = self.seive(right)
        primes = [num for num in range(left, right + 1) if sieveArr[num]]

        if len(primes) < 2:
            return [-1, -1]

        minDiff = float('inf')
        closetPair = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < minDiff:
                minDiff = diff
                closetPair = [primes[i - 1], primes[i]]
        return closetPair


left = 10
right = 19
print(Solution().closestPrimes(left, right))
left = 4
right = 6
print(Solution().closestPrimes(left, right))
