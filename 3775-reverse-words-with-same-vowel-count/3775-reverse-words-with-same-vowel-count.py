# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = set("aeiou")
        words = s.split()
        targetCount = sum(1 for c in words[0] if c in vowels)
        for i in range(1, len(words)):
            vowelCount = sum(1 for c in words[i] if c in vowels)
            if vowelCount == targetCount:
                words[i] = words[i][::-1]
        return " ".join(words)


s = "cat and mice"
print(Solution().reverseWords(s))
s = "book is nice"
print(Solution().reverseWords(s))
s = "banana healthy"
print(Solution().reverseWords(s))
