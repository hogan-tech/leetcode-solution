# time complexity: O(n + m*k)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        for char in chars:
            counts[char] += 1

        ans = 0
        for word in words:
            wordCounts = defaultdict(int)
            for wordChar in word:
                wordCounts[wordChar] += 1

            good = True
            for c, freq in wordCounts.items():
                if counts[c] < freq:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(Solution().countCharacters(words, chars))
