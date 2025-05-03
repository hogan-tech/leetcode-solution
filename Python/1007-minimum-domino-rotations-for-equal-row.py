# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(target):
            rotationsA = rotationsB = 0
            for i in range(n):
                if A[i] != target and B[i] != target:
                    return -1
                elif A[i] != target:
                    rotationsA += 1
                elif B[i] != target:
                    rotationsB += 1
            return min(rotationsA, rotationsB)

        n = len(A)
        rotations = check(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return check(B[0])


tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(Solution().minDominoRotations(tops, bottoms))
tops = [3, 5, 1, 2, 3]
bottoms = [3, 6, 3, 3, 4]
print(Solution().minDominoRotations(tops, bottoms))
