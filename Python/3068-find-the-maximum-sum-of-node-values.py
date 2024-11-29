# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        count = 0
        positiveMinimum = 1 << 30
        negativeMaximum = -1 * (1 << 30)

        for nodeValue in nums:
            operatedNodeValue = nodeValue ^ k
            sumVal += nodeValue
            netChange = operatedNodeValue - nodeValue
            if netChange > 0:
                positiveMinimum = min(positiveMinimum, netChange)
                sumVal += netChange
                count += 1
            else:
                negativeMaximum = max(negativeMaximum, netChange)

        if count % 2 == 0:
            return sumVal

        return max(sumVal - positiveMinimum, sumVal + negativeMaximum)


nums = [7, 7, 7, 7, 7, 7]
k = 3
edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]

print(Solution().maximumValueSum(nums, k, edges))
