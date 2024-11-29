# time complexity: O(n)
# space complexity: O(1)
from typing import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretFreq = Counter(secret)
        A = B = 0
        for i, c in enumerate(guess):
            if c in secretFreq:
                if c == secret[i]:
                    A += 1
                    B -= int(secretFreq[c] <= 0)
                else:
                    B += int(secretFreq[c] > 0)
            secretFreq[c] -= 1
        return "{}A{}B".format(A, B)


secret = "1123"
guess = "0111"
print(Solution().getHint(secret, guess))
