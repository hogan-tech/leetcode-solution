from typing import List


class Solution:
    def findAnagrams(self, original: str, target: str) -> List[int]:
        originalLen, targetLen = len(original), len(target)

        originalCount, targetCount = [0]*26, [0]*26

        for char in target:
            targetCount[ord(char) - ord('a')] += 1

        output = []
        for i in range(originalLen):
            originalCount[ord(original[i]) - ord('a')] += 1
            if i >= targetLen:
                originalCount[ord(original[i - targetLen]) - ord('a')] -= 1
            if targetCount == originalCount:
                output.append(i-targetLen+1)
        return output