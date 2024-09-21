# time complexity: O(k * c(9,k))
# space complexity: O(k)
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(remain: int, comb: List[int], nextStart: int):
            if remain == 0 and len(comb) == k:
                result.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            for i in range(nextStart, 9):
                comb.append(i + 1)
                backtrack(remain - i - 1, comb, i + 1)
                comb.pop()

        backtrack(n, [], 0)

        return result


k = 3
n = 7
print(Solution().combinationSum3(k, n))
