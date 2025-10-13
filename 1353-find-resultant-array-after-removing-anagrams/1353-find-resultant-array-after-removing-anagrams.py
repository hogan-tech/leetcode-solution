# time complexity: O(n^2*logn)
# space complexity: O(n)
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                result.append(words[i])
        return result


words = ["abba", "baba", "bbaa", "cd", "cd"]
print(Solution().removeAnagrams(words))
words = ["a", "b", "c", "d", "e"]
print(Solution().removeAnagrams(words))
