from typing import Counter


class Solution:
    def minimumPushes(self, words: str) -> int:
        wordCounter = list(Counter(words).values())
        wordCounter.sort(reverse=True)
        ans = 0
        for i in range(len(wordCounter)):
            ans += (i // 8 + 1) * wordCounter[i]
        return ans


words = "aabbccddeeffgghhiiiiii"
print(Solution().minimumPushes(words))
