# time complexity: O(n^2)
# space compelxity: O(n)
class Solution:
    def hasSameDigits(self, s: str) -> bool:

        while len(s) > 2:
            currS = ""
            for i in range(1, len(s)):
                currS += str((int(s[i]) + int(s[i - 1])) % 10)
            s = currS

        return s[0] == s[1]


s = "3902"
print(Solution().hasSameDigits(s))
s = "34789"
print(Solution().hasSameDigits(s))
