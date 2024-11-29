# time complexity: O(2^n)
# space complexity: O(2^n)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memoization = {}
        return self._dfs(s, word_set, memoization)

    def _dfs(self, remainingStr: str, wordSet: set, memoization: dict) -> List[str]:
        if remainingStr in memoization:
            return memoization[remainingStr]
        if not remainingStr:
            return [""]
        results = []
        for i in range(1, len(remainingStr) + 1):
            currentWord = remainingStr[:i]
            if currentWord in wordSet:
                for nextWord in self._dfs(remainingStr[i:], wordSet, memoization):
                    results.append(
                        currentWord + (" " if nextWord else "") + nextWord)
        memoization[remainingStr] = results
        return results


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, wordDict))
