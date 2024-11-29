# time complexity: O(n*m)
# space complexity: O(1)
from typing import Counter, List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tempCounter = Counter(words[0])
        for word in words:
            tempCounter &= Counter(word)
        return list(tempCounter.elements())


words = ["bella", "label", "roller"]
print(Solution().commonChars(words))
