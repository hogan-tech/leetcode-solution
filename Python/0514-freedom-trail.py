# time complexity: O(K*R^2)
# space complexity: O(K*R)
from cmath import inf


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ringLen = len(ring)
        keyLen = len(key)
        bestSteps = [[inf] * (keyLen + 1) for _ in range(ringLen)]

        def count_steps(curr, next):
            stepsBetween = abs(curr - next)
            stepsAround = ringLen - stepsBetween
            return min(stepsBetween, stepsAround)

        for row in bestSteps:
            row[keyLen] = 0

        for keyI in range(keyLen - 1, -1, -1):
            for ringI in range(ringLen):
                for charI in range(ringLen):
                    if ring[charI] == key[keyI]:
                        bestSteps[ringI][keyI] = min(
                            bestSteps[ringI][keyI],
                            1 + count_steps(ringI, charI)
                            + bestSteps[charI][keyI + 1])

        return bestSteps[0][0]


ring = "godding"
key = "gd"
