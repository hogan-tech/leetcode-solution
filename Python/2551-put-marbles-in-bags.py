# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairWeights = [weights[i] + weights[i + 1] for i in range(n - 1)]

        pairWeights.sort()

        answer = 0
        for i in range(k - 1):
            answer += pairWeights[n - 2 - i] - pairWeights[i]

        return answer


weights = [1, 3, 5, 1]
k = 2
print(Solution().putMarbles(weights, k))
weights = [1, 3]
k = 2
print(Solution().putMarbles(weights, k))
