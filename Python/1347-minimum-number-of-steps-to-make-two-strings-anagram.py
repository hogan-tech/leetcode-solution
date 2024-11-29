# time complexity: O(n)
# space complexity: O(1)
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s) - Counter(t)).total()


s = "bab"
t = "aba"
print(Solution().minSteps(s, t))
