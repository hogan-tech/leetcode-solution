# time complexity: O(n*k)
# space complexity: O(1)
from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for c in word:
                counts[c] += 1

        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        return True


words = ["abc", "aabc", "bc"]
print(Solution().makeEqual(words))
