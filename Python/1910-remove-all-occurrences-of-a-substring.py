# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            partIdx = s.index(part)
            leftS = s[:partIdx]
            rightS = s[partIdx + len(part):]
            s = leftS + rightS
        return s


s = "daabcbaabcbc"
part = "abc"
print(Solution().removeOccurrences(s, part))
s = "axxxxyyyyb"
part = "xy"
print(Solution().removeOccurrences(s, part))
s = "aabababa"
part = "aba"
print(Solution().removeOccurrences(s, part))
