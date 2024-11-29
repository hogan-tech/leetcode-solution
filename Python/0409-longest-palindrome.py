# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpair = 0
        count = 0
        for value in Counter(s).values():
            if value % 2 == 0:
                count += value
            else:
                if value > 2:
                    count += (value - 1)
                unpair = 1
        return count + unpair


s = "a"

print(Solution().longestPalindrome(s))
