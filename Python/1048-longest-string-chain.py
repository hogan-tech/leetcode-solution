from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}

        words.sort(key=lambda x: len(x))

        longestWordSequenceLength = 1

        for word in words:
            presentLength = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    previousLength = dp[predecessor]
                    presentLength = max(presentLength, previousLength + 1)

            dp[word] = presentLength
            longestWordSequenceLength = max(
                longestWordSequenceLength, presentLength)
        return longestWordSequenceLength


words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(Solution().longestStrChain(words))
