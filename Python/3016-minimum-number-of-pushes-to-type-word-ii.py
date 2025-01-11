# time complexity: O(nlogn)
# space complexity: O(n)
from typing import Counter


class Solution:
    def minimumPushes(self, words: str) -> int:
        wordCounter = list(Counter(words).values())
        wordCounter.sort(reverse=True)
        result = 0
        for i in range(len(wordCounter)):
            result += (i // 8 + 1) * wordCounter[i]
        return result


word = "abcde"
print(Solution().minimumPushes(word))
word = "xyzxyzxyzxyz"
print(Solution().minimumPushes(word))
word = "aabbccddeeffgghhiiiiii"
print(Solution().minimumPushes(word))
