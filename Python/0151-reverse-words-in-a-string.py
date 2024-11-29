# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


s = "  hello world  "
print(Solution().reverseWords(s))
