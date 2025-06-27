# Time Complexity: O(2^(n/2) * n)
# Space Complexity: O(2^(n/2))
from bisect import bisect_left
from typing import List
from itertools import combinations


class Solution:
    def getSubsequenceSumWithElements(self, arr):
        solution = {}
        n = len(arr)

        for k in range(1, n+1):
            sums = []
            allComb = combinations(arr, k)
            for comb in allComb:
                sums.append(sum(comb))

            solution[k] = sums

        return solution

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2

        firstHalf = nums[:half]
        secondHalf = nums[half:]

        firstSeq = self.getSubsequenceSumWithElements(firstHalf)
        secondSeq = self.getSubsequenceSumWithElements(secondHalf)

        solution = abs(sum(firstHalf) - sum(secondHalf))

        total = sum(nums)
        halfTotal = total//2

        for k in range(1, half):
            left_elements = firstSeq[k]
            right_elements = sorted(secondSeq[half-k])

            for summ in left_elements:
                target = halfTotal - summ
                nearestIdx = bisect_left(right_elements, target)

                for i in [nearestIdx-1, nearestIdx]:
                    if 0 <= i < len(right_elements):
                        leftSub = summ + right_elements[i]
                        rightSub = total - leftSub
                        solution = min(solution, abs(leftSub-rightSub))
        return solution


nums = [3, 9, 7, 3]
print(Solution().minimumDifference(nums))
nums = [-36, 36]
print(Solution().minimumDifference(nums))
nums = [2, -1, 0, 4, -2, -9]
print(Solution().minimumDifference(nums))
