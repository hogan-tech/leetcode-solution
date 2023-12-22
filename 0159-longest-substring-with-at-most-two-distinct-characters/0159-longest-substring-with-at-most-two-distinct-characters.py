# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        hashmap = defaultdict()
        maxLen = 2
        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == 3:
                delIdx = min(hashmap.values())
                del hashmap[s[delIdx]]
                left = delIdx + 1
            maxLen = max(maxLen, right - left)
        return maxLen


s = "ccaabbb"
print(Solution().lengthOfLongestSubstringTwoDistinct(s))
