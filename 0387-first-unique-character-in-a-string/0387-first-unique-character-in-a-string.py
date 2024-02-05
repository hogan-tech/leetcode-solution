from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounter = Counter(s)
        for idx, char in enumerate(s):
            if sCounter[char] == 1:
                return idx
        return -1


s = "loveleetcode"
print(Solution().firstUniqChar(s))
