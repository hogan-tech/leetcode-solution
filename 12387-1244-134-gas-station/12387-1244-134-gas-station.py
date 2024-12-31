# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        startIdx = 0
        currentGas = 0
        for i in range(len(gas)):
            currentGas = currentGas + (gas[i] - cost[i])
            if currentGas < 0:
                currentGas = 0
                startIdx = i + 1

        return startIdx


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
gas = [2, 3, 4]
cost = [3, 4, 3]
print(Solution().canCompleteCircuit(gas, cost))
