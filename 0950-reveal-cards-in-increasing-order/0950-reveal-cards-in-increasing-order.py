# time complexity: O(nlogn)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)
        deck.sort()
        result = [0] * len(deck)
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result


deck = [17, 13, 11, 2, 3, 5, 7]
print(Solution().deckRevealedIncreasing(deck))
