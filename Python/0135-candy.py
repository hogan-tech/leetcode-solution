from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        LR, RL, Sum = [1]*size, [1]*size, [0]*size
        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                LR[i] = LR[i-1] + 1
        for i in range(size-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                RL[i] = RL[i+1] + 1
        for i in range(size):
            Sum[i] = max(LR[i], RL[i])
        return sum(Sum)


ratings = [1, 0, 2]
print(Solution().candy(ratings))
