# time complexity: O(n**0.5 * logn)
# space complexity: O(logn)
class Solution:
    def smallestValue(self, n: int) -> int:
        def primeFactors(n):
            i = 2
            factors = []
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1:
                factors.append(n)
            return factors

        num = n
        seen = set()
        while num > 0:
            factors = primeFactors(num)
            if len(factors) == 1:
                return factors[0]
            num = sum(factors)
            if num in seen:
                break
            seen.add(num)
        return num


n = 15
print(Solution().smallestValue(n))
n = 3
print(Solution().smallestValue(n))
