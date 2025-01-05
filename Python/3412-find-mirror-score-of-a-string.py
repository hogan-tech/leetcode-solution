# time complexity: O(n)
# space complexity: O(1)
from collections import defaultdict, deque


class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {chr(i): chr(ord('a') + ord('z') - i)
                  for i in range(ord('a'), ord('z')+1)}
        unmarked = defaultdict(deque)
        score = 0
        for i, char in enumerate(s):
            mirrorChar = mirror[char]
            if unmarked[mirrorChar]:
                j = unmarked[mirrorChar].pop()
                score += i - j
            else:
                unmarked[char].append(i)

        return score


s = "aczzx"
print(Solution().calculateScore(s))
s = "abcdef"
print(Solution().calculateScore(s))
