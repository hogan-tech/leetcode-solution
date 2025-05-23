# time complexity: O(n*m)
# space complexity: O(n)
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [0] * len(s)
        for word in words:
            start = 0
            while start < len(s):
                idx = s.find(word, start)
                if idx >= 0:
                    bold[idx:idx + len(word)] = [1] * len(word)
                    start = idx + 1
                else:
                    break
        result = []
        for i, c in enumerate(s):
            if bold[i] and (i == 0 or not bold[i - 1]):
                result.append('<b>')
            result.append(c)
            if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
                result.append('</b>')
        return "".join(result)


s = "abcxyz123"
words = ["abc", "123"]
print(Solution().addBoldTag(s, words))
s = "aaabbb"
words = ["aa", "b"]
print(Solution().addBoldTag(s, words))
