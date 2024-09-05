# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelsList = []
        for c in s:
            if c in vowels:
                vowelsList.append(c)
        result = ""
        for i in range(len(s)):
            if s[i] in vowels:
                result += vowelsList.pop()
            else:
                result += s[i]
        return result


s = "hello"
print(Solution().reverseVowels(s))
