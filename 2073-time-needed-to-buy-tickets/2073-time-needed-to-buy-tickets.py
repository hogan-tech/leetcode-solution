# time complexity: O(n^2)
# space complexity: O(1)
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if i == k and tickets[i] == 0:
                        return time
        return time


tickets = [2, 3, 2]
k = 2
print(Solution().timeRequiredToBuy(tickets, k))
