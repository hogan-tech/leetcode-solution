from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getWords(i):
            currentLine = []
            currLength = 0

            while i < len(words) and currLength + len(words[i]) <= maxWidth:
                currentLine.append(words[i])
                currLength += len(words[i]) + 1
                i += 1

            return currentLine

        def createLine(line, i):
            baseLength = -1
            for word in line:
                baseLength += len(word) + 1

            extraSpaces = maxWidth - baseLength

            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extraSpaces

            wordCount = len(line) - 1
            spacesPerWord = extraSpaces // wordCount
            needsExtraSpace = extraSpaces % wordCount

            for j in range(needsExtraSpace):
                line[j] += " "

            for j in range(wordCount):
                line[j] += " " * spacesPerWord

            return " ".join(line)

        ans = []
        i = 0

        while i < len(words):
            currentLine = getWords(i)
            i += len(currentLine)
            ans.append(createLine(currentLine, i))

        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
