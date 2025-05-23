# time complexity: O(n*m)
# space complexity: O(n)
from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        bold = [0] * len(S)

        for word in words:
            start = 0
            while start < len(S):
                idx = S.find(word, start)
                if idx >= 0:
                    bold[idx:idx+len(word)] = [1] * len(word)
                    start = idx + 1
                else:
                    break

        result = []
        for i, c in enumerate(S):
            if bold[i] and (i == 0 or not bold[i - 1]):
                result.append('<b>')
            result.append(c)
            if bold[i] and (i == len(S) - 1 or not bold[i + 1]):
                result.append('</b>')

        return "".join(result)


words = ["ab", "bc"]
s = "aabcd"
print(Solution().boldWords(words, s))
words = ["ab", "cb"]
s = "aabcd"
print(Solution().boldWords(words, s))
