class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            if separator in word:
                result.extend(word.split(separator))
            else:
                result.append(word)
        return [i for i in result if i]