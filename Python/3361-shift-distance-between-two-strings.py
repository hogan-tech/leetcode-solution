# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        totalCost = 0
        for charS, charT in zip(s, t):
            if charS == charT:
                continue

            startIdx = ord(charS) - ord('a')
            targetIdx = ord(charT) - ord('a')

            forwardDistance = (targetIdx - startIdx) % 26
            backwardDistance = (startIdx - targetIdx) % 26

            forwardCost = sum(nextCost[(startIdx + i) % 26]
                              for i in range(forwardDistance))
            backwardCost = sum(previousCost[(startIdx - i) % 26]
                               for i in range(backwardDistance))

            totalCost += min(forwardCost, backwardCost)

        return totalCost


s = "abab"
t = "baba"
nextCost = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
previousCost = [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution().shiftDistance(s, t, nextCost, previousCost))
s = "leet"
t = "code"
nextCost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
previousCost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().shiftDistance(s, t, nextCost, previousCost))
