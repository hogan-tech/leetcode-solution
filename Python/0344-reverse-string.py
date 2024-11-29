# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return s


s = ["h", "e", "l", "l", "o"]
print(Solution().reverseString(s))
