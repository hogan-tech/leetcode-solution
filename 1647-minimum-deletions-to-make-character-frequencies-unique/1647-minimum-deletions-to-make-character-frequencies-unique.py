

from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        frequence = [0]*26
        for char in s:
            frequence[ord(char) - ord('a')] += 1
        frequence.sort(reverse=True)
        count = 0
        maxLen = len(s)
        for freq in frequence:
            if freq > maxLen:
                count += freq - maxLen
                freq = maxLen
            maxLen = max(0, freq - 1)
        return count


s = "aabbccc"
print(Solution().minDeletions(s))
