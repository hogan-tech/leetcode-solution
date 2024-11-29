# time complexity: O(n)
# space compelxity: O(n)
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
                res += 1
        return res


s = "abcd"
print(Solution().numberOfSpecialSubstrings(s))
