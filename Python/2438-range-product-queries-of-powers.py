# time complexity: O(logn + q)
# space complexity: O(logn + q)
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        binaryInt = bin(n)[2:][::-1]
        powers = []
        for i, num in enumerate(binaryInt):
            if num == "1":
                powers.append(2 ** i)
        prefix = [1 for _ in range(len(powers) + 1)]
        for i in range(len(powers)):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD

        result = []
        for start, end in queries:
            product = (prefix[end + 1] *
                       pow(prefix[start], MOD - 2, MOD)) % MOD
            result.append(product)

        return result


n = 15
queries = [[0, 1], [2, 2], [0, 3]]
print(Solution().productQueries(n, queries))
n = 2
queries = [[0, 0]]
print(Solution().productQueries(n, queries))
