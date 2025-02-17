# time complexity: O(sigma*P(n,k))
# space complexity: O(n)
from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []

        def backtrack(comb, counter):
            if comb not in result:
                result.append(list(comb))
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    comb.append(key)
                    backtrack(comb, counter)
                    counter[key] += 1
                    comb.pop()

        backtrack([], Counter(tiles))
        return len(result) - 1


tiles = "AAB"
print(Solution().numTilePossibilities(tiles))
tiles = "AAABBC"
print(Solution().numTilePossibilities(tiles))
tiles = "V"
print(Solution().numTilePossibilities(tiles))
