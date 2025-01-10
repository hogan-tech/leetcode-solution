# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        result = []
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j + 1] in words:
                    result.append([i, j])
        return result


text = "thestoryofleetcodeandme"
words = ["story", "fleet", "leetcode"]
print(Solution().indexPairs(text, words))
text = "ababa"
words = ["aba", "ab"]
print(Solution().indexPairs(text, words))
