# time complexity: O(2^n)
# space complexity: O(2^n)
from typing import List

# Top Down
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memoization = {}
        return self.dp(s, wordSet, memoization)
    def dp(self, remainingStr: str, wordSet: set, memoization: dict) -> List[str]:
        if remainingStr in memoization:
            return memoization[remainingStr]
        if not remainingStr:
            return [""]
        results = []
        for i in range(1, len(remainingStr) + 1):
            currentWord = remainingStr[:i]
            if currentWord in wordSet:
                for nextWord in self.dp(remainingStr[i:], wordSet, memoization):
                    results.append(
                        currentWord + (" " if nextWord else "") + nextWord)
        memoization[remainingStr] = results
        return results

# time complexity: O(n^2*v)
# space complexity: O(n^2*v)
# Bottom Up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            temp = []
            for j in range(i):
                suffix = prefix[j:]
                if suffix in wordDict:
                    for substring in dp[j]:
                        temp.append((substring + " " + suffix).strip())
            dp[i] = temp
        return dp[len(s)]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, wordDict))
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
