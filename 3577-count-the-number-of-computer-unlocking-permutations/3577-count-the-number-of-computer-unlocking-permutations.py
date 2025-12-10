# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(complexity)
        base = complexity[0]
        for i in range(1, n):
            if complexity[i] <= base:
                return 0

        result = 1
        for i in range(2, n):
            result = result * i % MOD
        return result


complexity = [1, 2, 3]
print(Solution().countPermutations(complexity))
complexity = [3, 3, 3, 4, 4, 4]
print(Solution().countPermutations(complexity))
