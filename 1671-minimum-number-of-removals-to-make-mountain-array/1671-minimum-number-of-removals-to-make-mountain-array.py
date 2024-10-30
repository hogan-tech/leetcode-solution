# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        lisLen = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = self.lowerBound(lis, v[i])

            if index == len(lis):
                lis.append(v[i])
            else:
                lis[index] = v[i]

            lisLen[i] = len(lis)

        return lisLen

    def lowerBound(self, lis: List[int], target: int) -> int:
        left, right = 0, len(lis)
        while left < right:
            mid = left + (right - left) // 2
            if lis[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        lisLength = self.getLongestIncreasingSubsequenceLength(nums)

        nums.reverse()
        ldsLength = self.getLongestIncreasingSubsequenceLength(nums)
        ldsLength.reverse()

        minRemovals = float("inf")
        for i in range(N):
            if lisLength[i] > 1 and ldsLength[i] > 1:
                minRemovals = min(
                    minRemovals, N - lisLength[i] - ldsLength[i] + 1
                )

        return minRemovals


nums = [1, 3, 1]
print(Solution().minimumMountainRemovals(nums))
