# time complexity: O(n)
# space complexity: O(min(m,n))
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


Input = "abcabcbb"
print(Solution().lengthOfLongestSubstring(Input))
