# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome

        palindrome = palindrome[:-1] + 'b'
        return palindrome


palindrome = "abccba"
print(Solution().breakPalindrome(palindrome))
palindrome = "a"
print(Solution().breakPalindrome(palindrome))
