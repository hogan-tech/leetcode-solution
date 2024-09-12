from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        count = 0
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowedSet:
                    break
                if i == len(word) - 1:
                    count += 1
        return count


allowed = "cad"
words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
print(Solution().countConsistentStrings(allowed, words))
