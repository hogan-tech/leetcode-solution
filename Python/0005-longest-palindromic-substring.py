# time complexity: O(n)
# space complexity: O(n)
# Manacher's Algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sPrime = "#" + "#".join(s) + "#"
        n = len(sPrime)
        palindromeRadii = [0] * n
        center = radius = 0
        for i in range(n):
            mirror = 2 * center - i
            if i < radius:
                palindromeRadii[i] = min(radius - i, palindromeRadii[mirror])
            while (
                i + 1 + palindromeRadii[i] < n
                and i - 1 - palindromeRadii[i] >= 0
                and sPrime[i + 1 + palindromeRadii[i]]
                == sPrime[i - 1 - palindromeRadii[i]]
            ):
                palindromeRadii[i] += 1
            if i + palindromeRadii[i] > radius:
                center = i
                radius = i + palindromeRadii[i]
        maxLength = max(palindromeRadii)
        centerIndex = palindromeRadii.index(maxLength)
        startIndex = (centerIndex - maxLength) // 2
        longestPalindrome = s[startIndex: startIndex + maxLength]

        return longestPalindrome


# Brute Force
# time complexity: O(n^3)
# space complexity: O(n^3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start: start + length]
        return ""

# time complexity: O(n^2)
# space complexity: O(n^2)
# Dynamic Programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        if n < 1:
            return s
        maxLen = 1
        maxStr = s[0]
        for right in range(n):
            dp[right][right] = True
            for left in range(right):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if right - left + 1 > maxLen:
                        maxLen = right - left + 1
                        maxStr = s[left:right + 1]

        return maxStr



s = "babad"
print(Solution().longestPalindrome(s))
s = "cbbd"
print(Solution().longestPalindrome(s))
