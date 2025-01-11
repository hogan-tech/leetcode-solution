# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def appealSum(self, s: str) -> int:
        track = defaultdict(lambda: -1)
        appeal = 0
        n = len(s)
        for i, c in enumerate(s):
            appeal += (i - track[c]) * (n - i)
            track[c] = i

        return appeal


s = "abbca"
print(Solution().appealSum(s))
s = "code"
print(Solution().appealSum(s))
