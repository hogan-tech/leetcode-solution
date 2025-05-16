# time complexity: O(n^2*l)
# space complexity: O(n)
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev = [-1] * n
        maxIdx = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxIdx]:
                maxIdx = i

        result = []
        i = maxIdx
        while i >= 0:
            result.append(words[i])
            i = prev[i]
        result.reverse()
        return result

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1


words = ["bab", "dab", "cab"]
groups = [1, 2, 2]
print(Solution().getWordsInLongestSubsequence(words, groups))
words = ["a", "b", "c", "d"]
groups = [1, 2, 3, 4]
print(Solution().getWordsInLongestSubsequence(words, groups))
