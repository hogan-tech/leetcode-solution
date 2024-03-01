from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return '1' * (s.count('1') - 1) + '0' * (len(s) - s.count('1')) + '1'


s = "010"
print(Solution().maximumOddBinaryNumber(s))
