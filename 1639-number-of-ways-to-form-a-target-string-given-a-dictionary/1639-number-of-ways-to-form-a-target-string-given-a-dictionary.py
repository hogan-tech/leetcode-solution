# time complexity: O(n*wordLen + targetLen * wordLen)
# space complexity: O(targetLen * wordLen)
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        alphabet = 26
        MOD = 1000000007
        targetLen = len(target)
        wordLen = len(words[0])
        charOccurrences = [[0] * wordLen for _ in range(alphabet)]

        for col in range(wordLen):
            for word in words:
                charOccurrences[ord(word[col]) - ord('a')][col] += 1

        dp = [[0] * (wordLen + 1) for _ in range(targetLen + 1)]

        dp[0][0] = 1
        for length in range(targetLen + 1):
            for col in range(wordLen):
                if length < targetLen:
                    dp[length + 1][col + 1] += (
                        charOccurrences[ord(target[length]) - ord('a')][col] * dp[length][col])
                    dp[length + 1][col + 1] %= MOD
                dp[length][col + 1] += dp[length][col]
                dp[length][col + 1] %= MOD
        return dp[targetLen][wordLen]


words = ["acca", "bbbb", "caca"]
target = "aba"
print(Solution().numWays(words, target))
