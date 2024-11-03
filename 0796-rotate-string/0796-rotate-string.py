class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False


s = "abcde"
goal = "cdeab"
print(Solution().rotateString(s, goal))
