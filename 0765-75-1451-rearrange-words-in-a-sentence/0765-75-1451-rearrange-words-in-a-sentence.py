# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def arrangeWords(self, text: str) -> str:
        wordsList = []
        for word in text.split(' '):
            wordsList.append((len(word), word.lower()))

        wordsList.sort(key=lambda x: x[0])
        for i in range(len(wordsList)):
            _, word = wordsList[i]
            wordsList[i] = word

        result = " ".join(wordsList)

        return result[0].upper() + result[1:]


text = "Leetcode is cool"
print(Solution().arrangeWords(text))
text = "Keep calm and code on"
print(Solution().arrangeWords(text))
