# time complexity: O(n*3^n)
# space complexity: O(1)
from functools import lru_cache


class Solution:
    def maxProduct(self, s: str) -> int:
        self.answer = 0

        @lru_cache(None)
        def dfs(i, word, word2):
            if i >= len(s):
                if word == word[::-1] and word2 == word2[::-1]:
                    self.answer = max(len(word) * len(word2), self.answer)
                return

            dfs(i + 1, word + s[i], word2)
            dfs(i + 1, word, word2 + s[i])
            dfs(i + 1, word, word2)

        dfs(0, '', '')
        return self.answer


s = "leetcodecom"
print(Solution().maxProduct(s))
