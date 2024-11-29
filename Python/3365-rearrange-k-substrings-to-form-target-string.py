# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if k == 1:
            return s == t

        substringSize = n // k

        sGroup = defaultdict(str)
        tGroup = defaultdict(str)

        for i in range(n):
            group = i // substringSize
            char = s[i]
            sGroup[group] += char

        for i in range(n):
            group = i // substringSize
            char = t[i]
            tGroup[group] += char

        sList = sorted(list(sGroup.values()))
        tList = sorted(list(tGroup.values()))

        return sList == tList


print(Solution().isPossibleToRearrange("abcd", "cdab", 2))  # Output: True
print(Solution().isPossibleToRearrange("aabbcc", "bbaacc", 3))  # Output: True
print(Solution().isPossibleToRearrange("aabbcc", "bbaacc", 2))  # Output: False
print(Solution().isPossibleToRearrange("nc", "cn", 1))  # Output: False
print(Solution().isPossibleToRearrange("jvdk", "vjdk", 2))  # Output: False
