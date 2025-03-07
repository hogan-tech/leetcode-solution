# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alphaDict = defaultdict(list)
        for c in word:
            alphaDict[c.lower()].append(c)

        count = 0
        for _, arr in alphaDict.items():
            if arr == sorted(arr, reverse=True) and arr[-1].isupper() and arr[0].islower():
                count += 1
        return count


word = "aaAbcBC"
print(Solution().numberOfSpecialChars(word))
word = "abc"
print(Solution().numberOfSpecialChars(word))
word = "AbBCab"
print(Solution().numberOfSpecialChars(word))
