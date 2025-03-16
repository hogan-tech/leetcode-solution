# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = Counter(s)
        maxVal = max(counter.values())
        charSet = set()
        for key, val in counter.items():
            if val == maxVal:
                charSet.add(key)

        result = ''
        for c in s[::-1]:
            if c in charSet:
                result += c
                charSet.remove(c)

        return result[::-1]


s = "aabcbbca"
print(Solution().lastNonEmptyString(s))
s = "abcd"
print(Solution().lastNonEmptyString(s))
