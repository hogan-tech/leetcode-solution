# time complexity: O(n!)
# space complexity: O(n)
from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        baseList = []
        result = []
        for i in range(1, n+1):
            baseList.append(i)
        baseList = list(combinations(baseList, k))
        for i, item in enumerate(baseList):
            result.append(list(item))
        return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)
            remain = n - first_num + 1
            available = remain - need

            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans

print(Solution().combine(4, 2))
