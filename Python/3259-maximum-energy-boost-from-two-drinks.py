class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        a# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dpA = [0] * n
        dpB = [0] * n
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        for i in range(1, n):
            dpA[i] = max(dpA[i - 1] + energyDrinkA[i], dpB[i - 1])
            dpB[i] = max(dpB[i - 1] + energyDrinkB[i], dpA[i - 1])
        return max(dpA[-1], dpB[-1])


energyDrinkA = [1, 3, 1]
energyDrinkB = [3, 1, 1]
print(Solution().maxEnergyBoost(energyDrinkA, energyDrinkB))
energyDrinkA = [4, 1, 1]
energyDrinkB = [1, 1, 3]
print(Solution().maxEnergyBoost(energyDrinkA, energyDrinkB))
