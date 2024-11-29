# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        lossesCount = {}

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            lossesCount[loser] = lossesCount.get(loser, 0) + 1

        zeroLose, oneLose = [], []
        for player in seen:
            count = lossesCount.get(player, 0)
            if count == 1:
                oneLose.append(player)
            elif count == 0:
                zeroLose.append(player)
        return [sorted(zeroLose), sorted(oneLose)]


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
           [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(Solution().findWinners(matches))
