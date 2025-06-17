# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = defaultdict(int)
        left = 0
        maxFreq = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            if right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
        

'''
l
    r
AABABBA

(r - l + 1) + maxFreq > k
l ++

freq = {
    A: 2
    B: 1
}

'''


s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
