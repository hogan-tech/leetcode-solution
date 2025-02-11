# time complexity: O(2^n)
# space complexity: O(n)
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        s = ['0' for _ in range(n)]

        def backtrack(index, flag):
            if index == n:
                result.append(''.join(s))
                return
            if not flag:
                backtrack(index + 1, True)
            s[index] = '1'
            backtrack(index + 1, False)
            s[index] = '0'

        backtrack(0, False)
        return result


n = 3
print(Solution().validStrings(n))
n = 1
print(Solution().validStrings(n))
