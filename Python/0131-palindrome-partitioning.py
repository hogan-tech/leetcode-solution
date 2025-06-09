# time complexity: O(n*2^n)
# space complexity: O(n)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s: str):
            return s == s[::-1]

        def backtrack(tempStr: str, comb: List[str]):
            if not tempStr:
                result.append(comb)
                return

            for i in range(1, len(tempStr) + 1):
                if isPalindrome(tempStr[:i]):
                    backtrack(tempStr[i:], comb + [tempStr[:i]])

        backtrack(s, [])
        return result


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = []

        def backtrack(left: int, comb: List[str]):
            if left >= len(s):
                result.append(list(comb))

            for right in range(left, len(s)):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    comb.append(s[left: right + 1])
                    backtrack(right + 1, comb)
                    comb.pop()

        backtrack(0, [])
        return result


s = "aab"
print(Solution().partition(s))
s = "a"
print(Solution().partition(s))
