# time complexity: O(n)
# space complexity: O(1)
class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strList = [c.lower() for c in s if c.isalnum()]
        return strList == strList[::-1]


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
s = "race a car"
print(Solution().isPalindrome(s))
s = " "
print(Solution().isPalindrome(s))
