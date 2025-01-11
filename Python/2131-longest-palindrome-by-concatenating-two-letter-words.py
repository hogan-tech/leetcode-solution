# time complexity: O(n + min(n, 26 ^ 2))
# space complexity: O(min(n, 26 ^ 2))
from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqs = Counter(words)
        count = 0
        central = False
        for word, freq in freqs.items():
            if word[0] == word[1]:
                if freq % 2:
                    count += freq - 1
                    central = True
                else:
                    count += freq
            elif word[1] > word[0]:
                count += 2 * min(freq, freqs[word[1] + word[0]])

        if central:
            count += 1

        return 2 * count


words = ["lc", "cl", "gg"]
print(Solution().longestPalindrome(words))
words = ["ab", "ty", "yt", "lc", "cl", "ab"]
print(Solution().longestPalindrome(words))
words = ["cc", "ll", "xx"]
print(Solution().longestPalindrome(words))
