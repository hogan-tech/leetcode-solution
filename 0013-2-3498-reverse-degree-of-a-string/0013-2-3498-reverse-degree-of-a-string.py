# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def reverseDegree(self, s: str) -> int:
        def getScore(c):
            return 26 - (ord(c) - ord('a'))
        result = 0
        for i, c in enumerate(s):
            result += (i + 1) * getScore(c)
        return result


s = "abc"
print(Solution().reverseDegree(s))
s = "zaza"
print(Solution().reverseDegree(s))
