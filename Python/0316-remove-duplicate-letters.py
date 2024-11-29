from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        position = 0
        for i in range(len(s)):
            if s[i] < s[position]:
                position = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break

        return s[position] + self.removeDuplicateLetters(s[position:].replace(s[position], "")) if s else ""
