# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s) + 1
        factorials = [1] * n
        inverse = [1] * n

        def quickInverse(base: int, exponent: int, modulus: int):
            result = 1
            while exponent != 0:
                if (exponent & 1) == 1:
                    result = result * base % modulus
                exponent >>= 1
                base = base * base % modulus
            return result

        def combination(n: int, k: int, factorials: List[int], inverse: List[int]):
            return (factorials[n] * inverse[k] % MOD) * inverse[n-k] % MOD

        for i in range(1, n):
            factorials[i] = factorials[i-1] * i % MOD
            inverse[i] = quickInverse(factorials[i], MOD - 2, MOD)

        freq = [0] * 26
        maxCount = 1
        for char in s:
            maxCount = max(maxCount, freq[ord(char) - ord('a')] + 1)
            freq[ord(char) - ord('a')] += 1

        finalCount = 0
        for i in range(1, maxCount + 1):
            count = 1
            for j in range(26):
                if freq[j] >= i:
                    count = count * \
                        (combination(freq[j], i,
                         factorials, inverse) + 1) % MOD

            finalCount = (finalCount + count - 1) % MOD

        return int(finalCount)


s = "aabb"
print(Solution().countGoodSubsequences(s))
s = "leet"
print(Solution().countGoodSubsequences(s))
s = "abcd"
print(Solution().countGoodSubsequences(s))
s = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
print(Solution().countGoodSubsequences(s))
