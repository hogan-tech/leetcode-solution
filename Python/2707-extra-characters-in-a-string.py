# time complexity: O(n^3)
# space complexity: O(n+m*k)
from functools import lru_cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionarySet = len(s), set(dictionary)

        @lru_cache(None)
        def dp(start):
            if start == n:
                return 0
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end+1]
                if curr in dictionarySet:
                    ans = min(ans, dp(end+1))
            return ans
        return dp(0)


s = "leetscode"
dictionary = ["leet", "code", "leetcode"]

print(Solution().minExtraChar(s, dictionary))
