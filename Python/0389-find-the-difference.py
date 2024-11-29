# time complexity: O(n)
# space complexity: O(1)
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for key in (Counter(t) - Counter(s)).keys():
            return key


s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s, t))
s = ""
t = "y"
print(Solution().findTheDifference(s, t))
