# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total = sum(balance)
        if total < 0:
            return -1
        negIdx = -1
        for i in range(n):
            if balance[i] < 0:
                negIdx = i
                break
        if negIdx == -1:
            return 0
        need = -balance[negIdx]
        donors = []
        for i in range(n):
            if i != negIdx and balance[i] > 0:
                dist = min((i - negIdx) % n, (negIdx - i) % n)
                donors.append((dist, balance[i]))
        donors.sort()
        moves = 0
        for dist, amount in donors:
            if need == 0:
                break
            take = min(need, amount)
            moves += take * dist
            need -= take
        return moves if need == 0 else -1


balance = [5, 1, -4]
print(Solution().minMoves(balance))
balance = [1, 2, -5, 2]
print(Solution().minMoves(balance))
balance = [-3, 2]
print(Solution().minMoves(balance))
