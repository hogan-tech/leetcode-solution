# time complexity: O(2^n)
# space complexity: O(n)
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        def backtrack(path: List):
            if len(path) == n:
                if path[0] == 0:
                    return
                result.append(int("".join([str(num) for num in path])))
                return

            for i in range(10):
                num = digits[i]
                if len(path) == 0:
                    path.append(num)
                    backtrack(path)
                    path.pop()
                elif abs(num - path[-1]) == k:
                    path.append(num)
                    backtrack(path)
                    path.pop()
            return

        backtrack([])
        return result


n = 3
k = 7
print(Solution().numsSameConsecDiff(n, k))
n = 2
k = 1
print(Solution().numsSameConsecDiff(n, k))
