# time complexity: O(n^4)
# space complexity: O(n)
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        result = 0

        def isPalindrome(x: str) -> bool:
            return x == x[::-1]

        n, m = len(s), len(t)

        for i in range(n + 1):
            for j in range(i, n + 1):
                sSub = s[i:j]

                for k in range(m + 1):
                    for l in range(k, m + 1):
                        tSub = t[k:l]
                        combined = sSub + tSub
                        if isPalindrome(combined):
                            result = max(result, len(combined))

        return result


s = "a"
t = "a"
print(Solution().longestPalindrome(s, t))
s = "abc"
t = "def"
print(Solution().longestPalindrome(s, t))
s = "b"
t = "aaaa"
print(Solution().longestPalindrome(s, t))
s = "abcde"
t = "ecdba"
print(Solution().longestPalindrome(s, t))
