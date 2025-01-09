# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(Solution().prefixCount(words, pref))
words = ["leetcode", "win", "loops", "success"]
pref = "code"
print(Solution().prefixCount(words, pref))
