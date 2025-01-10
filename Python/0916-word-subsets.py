# time complexity: O(a+b)
# space complexity: O(a.l + b.l)
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word: str):
            countFreq = [0] * 26
            for c in word:
                countFreq[ord(c) - ord('a')] += 1
            return countFreq

        targetFreq = [0] * 26
        for word in words2:
            for i, value in enumerate(count(word)):
                targetFreq[i] = max(targetFreq[i], value)
        result = []
        for word in words1:
            if all(value1 >= value2 for value1, value2 in zip(count(word), targetFreq)):
                result.append(word)
        return result


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
print(Solution().wordSubsets(words1, words2))
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]
print(Solution().wordSubsets(words1, words2))
