# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return (count + 1) * count // 2


s = "abada"
c = "a"
print(Solution().countSubstrings(s, c))
s = "zzz"
c = "z"
print(Solution().countSubstrings(s, c))
