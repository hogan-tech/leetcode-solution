# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i].find(words[j]) != -1:
                    result.append(words[j])
        return list(set(result))


words = ["mass", "as", "hero", "superhero"]
print(Solution().stringMatching(words))
words = ["leetcode", "et", "code"]
print(Solution().stringMatching(words))
words = ["blue", "green", "bu"]
print(Solution().stringMatching(words))
words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
print(Solution().stringMatching(words))
