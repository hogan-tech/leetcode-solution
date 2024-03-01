# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oneFreq = s.count('1')
        return '1' * (oneFreq - 1) + '0' * (len(s) - oneFreq) + '1'


s = "010"
print(Solution().maximumOddBinaryNumber(s))
