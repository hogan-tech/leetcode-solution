# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        digit = 0
        result = []
        for c in word:
            digit = (digit * 10 + int(c)) % m
            result.append(int(digit == 0))
        return result


word = "998244353"
m = 3
print(Solution().divisibilityArray(word, m))
word = "1010"
m = 10
print(Solution().divisibilityArray(word, m))
