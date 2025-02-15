# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        heapify(players)
        heapify(trainers)
        while players and trainers:
            if players[0] <= trainers[0]:
                heappop(players)
                heappop(trainers)
                count += 1
            else:
                heappop(trainers)

        return count


players = [4, 7, 9]
trainers = [8, 2, 5, 8]
print(Solution().matchPlayersAndTrainers(players, trainers))
players = [1, 1, 1]
trainers = [10]
print(Solution().matchPlayersAndTrainers(players, trainers))
