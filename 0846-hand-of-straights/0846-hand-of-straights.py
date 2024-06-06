# time complexity: O(n*m)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        handCounter = Counter(hand)
        if len(hand) % groupSize:
            return False
        for num in hand:
            if handCounter[num]:
                for currNum in range(num, num+groupSize):
                    handCounter[currNum] -= 1
                    if handCounter[currNum] < 0:
                        return False
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(Solution().isNStraightHand(hand, groupSize))
