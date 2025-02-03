# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        space = [capacity[i] - rocks[i] for i in range(len(capacity))]
        space.sort()
        result = 0
        for i in range(len(space)):
            if space[i] == 0:
                result += 1
                continue
            if additionalRocks >= space[i]:
                additionalRocks -= space[i]
                space[i] = 0
                result += 1
            elif additionalRocks < space[i]:
                space[i] -= additionalRocks
                return result
        return result


capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2
print(Solution().maximumBags(capacity, rocks, additionalRocks))
capacity = [10, 2, 2]
rocks = [2, 2, 0]
additionalRocks = 100
print(Solution().maximumBags(capacity, rocks, additionalRocks))
