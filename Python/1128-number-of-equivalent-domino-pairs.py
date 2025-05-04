# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        for domino in dominoes:
            freq[tuple(sorted(domino))] += 1

        result = 0
        for value in freq.values():
            result += (value - 1) * value // 2

        return result


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
print(Solution().numEquivDominoPairs(dominoes))
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
print(Solution().numEquivDominoPairs(dominoes))
