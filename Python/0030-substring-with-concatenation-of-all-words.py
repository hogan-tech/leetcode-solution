# time complexity: O(a + n*b)
# space complexity: O(a + b)
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        sSize = len(s)
        wordLen = len(words[0])
        wordCount = Counter(words)

        def slidingWindow(left):
            foundCount = defaultdict(lambda: 0)
            totalMatched = 0
            for right in range(left, len(s), wordLen):
                if right + wordLen > sSize:
                    break
                newWord = s[right: right + wordLen]
                if newWord not in wordCount:
                    foundCount = defaultdict(lambda: 0)
                    totalMatched = 0
                    left = right + wordLen
                else:
                    foundCount[newWord] += 1
                    if foundCount[newWord] > wordCount[newWord]:
                        while foundCount[newWord] > wordCount[newWord]:
                            leftMost = s[left: left + wordLen]
                            foundCount[leftMost] -= 1
                            left += wordLen
                            if leftMost != newWord:
                                totalMatched -= 1
                    else:
                        totalMatched += 1
                if totalMatched == len(words):
                    result.append(left)

        for i in range(wordLen):
            slidingWindow(i)

        return result


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(Solution().findSubstring(s, words))
