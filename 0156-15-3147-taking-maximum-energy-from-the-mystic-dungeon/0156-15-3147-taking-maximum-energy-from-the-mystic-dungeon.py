# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        transport = [0] * len(energy)
        for i in range(k):
            transport[i] = energy[i]
        for i in range(k, len(energy)):
            transport[i] += transport[i - k] + energy[i]
        return max(transport)


'''
5 2 -10 -5 1
0 3 -10 -5 1
'''
energy = [5, 2, -10, -5, 1]
k = 3
print(Solution().maximumEnergy(energy, k))
energy = [-2, -3, -1]
k = 2
print(Solution().maximumEnergy(energy, k))
