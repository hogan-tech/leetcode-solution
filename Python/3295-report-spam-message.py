# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        bannedWordsSet = set(bannedWords)
        for word in message:
            if word in bannedWordsSet:
                count += 1
                if count >= 2:
                    return True
        return False


message = ["t", "j", "w", "g", "x", "v", "b", "j"]
bannedWords = ["e", "q", "s", "j", "q", "w", "k", "w"]
print(Solution().reportSpam(message, bannedWords))
