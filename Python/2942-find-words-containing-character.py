# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result


words = ["leet", "code"]
x = "e"
print(Solution().findWordsContaining(words, x))
