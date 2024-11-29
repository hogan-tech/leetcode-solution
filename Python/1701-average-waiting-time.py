# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        nextIdleTime = 0
        waitTime = 0
        for customer in customers:
            arrival = customer[0]
            time = customer[1]
            nextIdleTime = max(arrival, nextIdleTime) + time
            waitTime += nextIdleTime - arrival
        return waitTime / len(customers)


customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(Solution().averageWaitingTime(customers))
