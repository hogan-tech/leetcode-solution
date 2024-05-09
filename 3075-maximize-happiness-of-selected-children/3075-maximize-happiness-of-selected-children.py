# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happinessSum = 0
        turns = 0
        for i in range(k):
            happinessSum += max(happiness[i] - turns, 0)
            turns += 1

        return happinessSum


happiness = [12, 1, 42]
k = 3
print(Solution().maximumHappinessSum(happiness, k))
