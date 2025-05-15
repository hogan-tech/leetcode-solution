# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        prev = -1
        for i in range(len(words)):
            word = words[i]
            group = groups[i]
            if group != prev:
                result.append(word)
                prev = group
        return result


words = ["e", "a", "b"]
groups = [0, 0, 1]
print(Solution().getLongestSubsequence(words, groups))
words = ["a", "b", "c", "d"]
groups = [1, 0, 1, 1]
print(Solution().getLongestSubsequence(words, groups))
