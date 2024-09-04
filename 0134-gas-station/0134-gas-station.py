# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGain = 0
        currGain = 0
        answer = 0

        for i in range(len(gas)):
            totalGain += gas[i] - cost[i]
            currGain += gas[i] - cost[i]

            if currGain < 0:
                currGain = 0
                answer = i + 1

        return answer if totalGain >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(Solution().canCompleteCircuit(gas, cost))
