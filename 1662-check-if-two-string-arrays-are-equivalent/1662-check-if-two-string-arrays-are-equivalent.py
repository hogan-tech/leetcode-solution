# time complexity: O(n*k)
# space complexity: O(n*k)
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for i in range(len(word1)):
            str1 += word1[i]
        for i in range(len(word2)):
            str2 += word2[i]
        return str1 == str2


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2))
