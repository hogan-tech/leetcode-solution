# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        currA, currB = capacityA, capacityB
        left, right = 0, len(plants) - 1
        count = 0
        while left < right:
            if capacityA < plants[left]:
                capacityA = currA
                count += 1
            capacityA -= plants[left]
            left += 1

            if capacityB < plants[right]:
                capacityB = currB
                count += 1
            capacityB -= plants[right]
            right -= 1

        if left == right:
            if max(capacityA, capacityB) < plants[left]:
                count += 1

        return count


plants = [2, 2, 3, 3]
capacityA = 5
capacityB = 5
print(Solution().minimumRefill(plants, capacityA, capacityB))
plants = [2, 2, 3, 3]
capacityA = 3
capacityB = 4
print(Solution().minimumRefill(plants, capacityA, capacityB))
plants = [5]
capacityA = 10
capacityB = 8
print(Solution().minimumRefill(plants, capacityA, capacityB))
plants = [1, 2, 4, 4, 5]
capacityA = 6
capacityB = 5
print(Solution().minimumRefill(plants, capacityA, capacityB))
