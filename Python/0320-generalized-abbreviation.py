# time complexity: O(2^n)
# space complexity: O(n)
from typing import List


class Solution:
    def storeAbbreviations(
        self,
        abbreviations: List[str],
        word: str,
        currWord: str,
        index: int,
        abbreviatedCount: int
    ):
        if index == len(word):
            if abbreviatedCount > 0:
                currWord += str(abbreviatedCount)
            abbreviations.append(currWord)
            return

        self.storeAbbreviations(
            abbreviations,
            word,
            currWord
            + (str(abbreviatedCount) if abbreviatedCount > 0 else "")
            + word[index],
            index + 1,
            0
        )

        self.storeAbbreviations(
            abbreviations, word, currWord, index + 1, abbreviatedCount + 1
        )

    def generateAbbreviations(self, word: str) -> List[str]:
        abbreviations = []
        self.storeAbbreviations(abbreviations, word, "", 0, 0)
        return abbreviations


word = "word"
print(Solution().generateAbbreviations(word))
