# time complexity: O(n)
# space complexity: O(n)
from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        for i in range(len(s) - 1):
            first, second = s[i], s[i + 1]
            if first != second:
                if freq[first] == int(first) and freq[second] == int(second):
                    return first + second

        return ""


s = "2523533"
print(Solution().findValidPair(s))  # 23
s = "221"
print(Solution().findValidPair(s))  # 21
s = "22"
print(Solution().findValidPair(s))  # ""
s = "1522"
print(Solution().findValidPair(s))  # ""
