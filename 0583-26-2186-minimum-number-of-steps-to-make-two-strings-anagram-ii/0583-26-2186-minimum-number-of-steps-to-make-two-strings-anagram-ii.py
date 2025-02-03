# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        stCounter = sCounter - tCounter
        tsCounter = tCounter - sCounter
        result = 0
        for _, value in stCounter.items():
            result += value
        for _, value in tsCounter.items():
            result += value
        return result


s = "leetcode"
t = "coats"
print(Solution().minSteps(s, t))
s = "night"
t = "thing"
print(Solution().minSteps(s, t))
