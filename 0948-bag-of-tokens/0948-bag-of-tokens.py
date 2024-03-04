# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        score = 0
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power -= tokens[i]
                i += 1
            elif score >= 1 and i < j:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return score


tokens = [100]
power = 50
print(Solution().bagOfTokensScore(tokens, power))
