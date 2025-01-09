# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    class Trie:
        def __init__(self):
            self.children = [None] * 10
            self.isVisited = False

    def equalDigitFrequency(self, s: str) -> int:
        root = self.Trie()
        totalValidSubstrings = 0

        for left in range(len(s)):
            currentNode = root
            digitFreq = [0] * 10
            uniDigitCount = 0
            maxDigitFreq = 0
            for right in range(left, len(s)):
                currentDigit = int(s[right])
                if digitFreq[currentDigit] == 0:
                    uniDigitCount += 1
                digitFreq[currentDigit] += 1
                maxDigitFreq = max(maxDigitFreq, digitFreq[currentDigit])

                if not currentNode.children[currentDigit]:
                    currentNode.children[currentDigit] = self.Trie()
                currentNode = currentNode.children[currentDigit]

                if uniDigitCount * maxDigitFreq == right - left + 1 and not currentNode.isVisited:
                    totalValidSubstrings += 1
                    currentNode.isVisited = True
        return totalValidSubstrings


s = "1212"
print(Solution().equalDigitFrequency(s))
s = "12321"
print(Solution().equalDigitFrequency(s))
