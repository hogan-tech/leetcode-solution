from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        prefix = [0 for _ in range(len(possible))]
        suffix = [0 for _ in range(len(possible))]
        prefix[0] = 1 if possible[0] else -1
        suffix[-1] = 1 if possible[-1] else -1
        
        for i in range(1, len(possible)):
            prefix[i] = prefix[i - 1] + (1 if possible[i] else -1)
        for i in range(len(possible)-2, -1, -1):
            suffix[i] = suffix[i + 1] + (1 if possible[i] else -1)
        
        for i in range(len(possible) - 1):
            if prefix[i] > suffix[i + 1]:
                return i + 1
        return -1


possible = [1, 0, 1, 0]
print(Solution().minimumLevels(possible))
possible = [1, 1, 1, 1, 1]
print(Solution().minimumLevels(possible))
possible = [0, 0]
print(Solution().minimumLevels(possible))
