# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = k - 1
        right = n - 1
        remainTotal = sum(cardPoints[: k])
        result = remainTotal
        for _ in range(k):
            remainTotal += (cardPoints[right] - cardPoints[left])
            result = max(result, remainTotal)
            left -= 1
            right -= 1
        return result


'''
      l     r
o o o x x x x
      l     r
o o x x x x o
o x x x x o o
x x x x o o o

remain = Total - currWindowTotal
nextTotal = remain + cardPoints[right] - cardPoints[left - 1]

'''

cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(Solution().maxScore(cardPoints, k))
cardPoints = [2, 2, 2]
k = 2
print(Solution().maxScore(cardPoints, k))
cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
print(Solution().maxScore(cardPoints, k))
