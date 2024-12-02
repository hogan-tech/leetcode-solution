# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return i + 1
        return -1


sentence = "i love eating burger"
searchWord = "burg"
print(Solution().isPrefixOfWord(sentence, searchWord))
sentence = "this problem is an easy problem"
searchWord = "pro"
print(Solution().isPrefixOfWord(sentence, searchWord))
sentence = "i am tired"
searchWord = "you"
print(Solution().isPrefixOfWord(sentence, searchWord))
