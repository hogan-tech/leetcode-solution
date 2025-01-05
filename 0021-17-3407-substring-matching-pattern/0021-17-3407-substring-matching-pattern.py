# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, _, suffix = p.partition('*')
        startIdx = s.find(prefix)
        if startIdx == -1:
            return False
        remainS = s[startIdx + len(prefix):]
        return suffix in remainS


s = "leetcode"
p = "ee*e"
print(Solution().hasMatch(s, p))
s = "car"
p = "c*v"
print(Solution().hasMatch(s, p))
s = "luck"
p = "u*"
print(Solution().hasMatch(s, p))
s = "jjv"
p = "*j"
print(Solution().hasMatch(s, p))
