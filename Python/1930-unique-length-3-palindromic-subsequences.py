# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])


s = "aabca"

print(Solution().countPalindromicSubsequence(s))
