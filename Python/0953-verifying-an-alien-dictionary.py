# time complexity: O(w*m)
# space complexity: O(1)
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if order.find(c1) > order.find(c2):
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))
words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
print(Solution().isAlienSorted(words, order))
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))
