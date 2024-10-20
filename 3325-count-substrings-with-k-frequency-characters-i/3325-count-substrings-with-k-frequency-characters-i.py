# time complexity: O(n^2)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        totalSubstrings = 0
        n = len(s)
        charCount = defaultdict(int)
        left = 0

        for right in range(n):
            charCount[s[right]] += 1
            while any(count >= k for count in charCount.values()):
                totalSubstrings += n - right
                charCount[s[left]] -= 1
                left += 1

        return totalSubstrings


s = "abacb"
k = 2
print(Solution().numberOfSubstrings(s, k))


s = "abcde"
k = 1
print(Solution().numberOfSubstrings(s, k))
