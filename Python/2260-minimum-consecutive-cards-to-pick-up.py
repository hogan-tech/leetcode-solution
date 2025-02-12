# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardDict = defaultdict(int)
        result = float('inf')
        for i, card in enumerate(cards):
            if card in cardDict:
                result = min(result, i - cardDict[card] + 1)
            cardDict[card] = i
        return result if result != float('inf') else -1


cards = [3, 4, 2, 3, 4, 7]
print(Solution().minimumCardPickup(cards))
cards = [1, 0, 5, 3]
print(Solution().minimumCardPickup(cards))
