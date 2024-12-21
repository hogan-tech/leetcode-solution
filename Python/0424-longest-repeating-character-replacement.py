# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = right = 0
        freq = defaultdict(int)
        mostFreqChar = 0
        for right in range(len(s)):
            freq[s[right]] += 1

            mostFreqChar = max(mostFreqChar, freq[s[right]])

            if right - left + 1 - mostFreqChar > k:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result


s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
