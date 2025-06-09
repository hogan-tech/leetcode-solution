# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for right in range(n):
            dp[right][right] = True
            for left in range(right):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
        
        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
        
        return count


s = "abc"
print(Solution().countSubstrings(s))
s = "aaa"
print(Solution().countSubstrings(s))
