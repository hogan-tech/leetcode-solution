# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def addMinimum(self, word: str) -> int:
        prev = 'z'
        targetCount = 0
        for c in word:
            if c <= prev:
                targetCount += 1
            prev = c

        return targetCount * 3 - len(word)


word = "b"
print(Solution().addMinimum(word))
word = "aaa"
print(Solution().addMinimum(word))
word = "abc"
print(Solution().addMinimum(word))
word = "acb"
print(Solution().addMinimum(word))
word = "acab"
print(Solution().addMinimum(word))
