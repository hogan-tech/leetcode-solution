class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ""
        reversed = False
        for c in word:
            result += c
            if c == ch and not reversed:
                result = result[::-1]
                reversed = True
        return result


word = "abcdefd"
ch = "d"

print(Solution().reversePrefix(word, ch))
