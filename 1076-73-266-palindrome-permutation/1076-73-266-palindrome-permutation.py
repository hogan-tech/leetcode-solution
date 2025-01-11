# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        count = 0
        for value in freq.values():
            if value % 2 == 1:
                count += 1
        return count < 2


s = "code"
print(Solution().canPermutePalindrome(s))
s = "aab"
print(Solution().canPermutePalindrome(s))
s = "carerac"
print(Solution().canPermutePalindrome(s))
