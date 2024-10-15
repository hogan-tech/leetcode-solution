# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        freq = defaultdict(int)
        for i, c in enumerate(word):
            if c in "aeiou":
                if not i or word[i - 1] not in "aeiou":
                    anchor = j = i
                    freq.clear()
                freq[c] += 1
                while len(freq) == 5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1
                ans += j - anchor
        return ans


word = "aeiouu"
print(Solution().countVowelSubstrings(word))
