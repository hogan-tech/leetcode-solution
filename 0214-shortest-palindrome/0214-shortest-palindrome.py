# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        modifiedString = self.preprocessString(s)
        n = len(modifiedString)
        palindromeRadiusArray = [0] * n
        center = 0
        rightBoundary = 0
        maxPalindromeLength = 0
        for i in range(1, n - 1):
            mirrorIndex = 2 * center - i
            if rightBoundary > i:
                palindromeRadiusArray[i] = min(
                    rightBoundary - i, palindromeRadiusArray[mirrorIndex]
                )
            while (
                modifiedString[i + 1 + palindromeRadiusArray[i]]
                == modifiedString[i - 1 - palindromeRadiusArray[i]]
            ):
                palindromeRadiusArray[i] += 1
            if i + palindromeRadiusArray[i] > rightBoundary:
                center = i
                rightBoundary = i + palindromeRadiusArray[i]
            if i - palindromeRadiusArray[i] == 1:
                maxPalindromeLength = max(
                    maxPalindromeLength, palindromeRadiusArray[i]
                )
        suffix = s[maxPalindromeLength:][::-1]
        return suffix + s

    def preprocessString(self, s: str) -> str:
        return "^" + "#" + "#".join(s) + "#$"


s = "abcd"
print(Solution().shortestPalindrome(s))
