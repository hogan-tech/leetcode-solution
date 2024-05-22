from typing import Dict

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.backtrack(pattern, s, {})

    def backtrack(self, pattern: str, s: str, lookup: Dict[str, str]) -> bool:
        if pattern == "" or s == "":
            return pattern == "" and s == "" and len(set(lookup.values())) == len(set(lookup))

        firstPattern = pattern[0]
        if firstPattern in lookup:
            if s.startswith(lookup[firstPattern]):
                return self.backtrack(pattern[1:], s[len(lookup[firstPattern]):], lookup)
            else:
                return False

        n = len(s)
        for i in range(1, n + 1):
            lookup[firstPattern] = s[:i]
            result = self.backtrack(pattern[1:], s[i:], lookup)
            if result:
                return True

        del lookup[firstPattern]
        return False


pattern = "abab"
s = "redblueredblue"
print(Solution().wordPatternMatch(pattern, s))
