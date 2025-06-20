class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        result = 0
        currGain = 0
        for i in range(len(gas)):
            currGain += (gas[i] - cost[i])
            if currGain < 0:
                currGain = 0
                result = i + 1
        return result