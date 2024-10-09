# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = [-1, -1, -1]
        for triplet in triplets:
            if (triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]):
                temp[0] = max(triplet[0], temp[0])
                temp[1] = max(triplet[1], temp[1])
                temp[2] = max(triplet[2], temp[2])
        return temp == target


triplets = [[1, 3, 1]]
target = [1, 3, 2]
print(Solution().mergeTriplets(triplets, target))
