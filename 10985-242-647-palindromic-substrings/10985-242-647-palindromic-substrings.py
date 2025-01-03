# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for i in range(n - 1):
            dp[i][i+1] = (s[i] == s[i+1])
            count += dp[i][i+1]

        for length in range(3, n + 1):
            i = 0
            for j in range(length - 1, n):
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                count +=  dp[i][j]
                i += 1

        return count


s = "abc"
print(Solution().countSubstrings(s))
s = "aaa"
print(Solution().countSubstrings(s))
