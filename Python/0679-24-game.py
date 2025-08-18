# time complexity: O(n^3 * 3^(n-1) * n! * (n-1)!)
# space complexity: O(n^2)
from typing import List


class Solution:
    def generate_possible_results(self, a: float, b: float) -> List[float]:
        result = [a + b, a - b, b - a, a * b]
        if a:
            result.append(b / a)
        if b:
            result.append(a / b)
        return result

    def checkIfResultReached(self, cards: List[float]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.1
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                newList = [number for k, number in enumerate(
                    cards) if (k != i and k != j)]
                for res in self.generate_possible_results(cards[i], cards[j]):
                    newList.append(res)
                    if self.checkIfResultReached(newList):
                        return True
                    newList.pop()

        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self.checkIfResultReached(cards)


cards = [4, 1, 8, 7]
print(Solution().judgePoint24(cards))
cards = [1, 2, 1, 2]
print(Solution().judgePoint24(cards))
