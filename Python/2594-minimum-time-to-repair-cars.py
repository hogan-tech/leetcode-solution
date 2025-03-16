# time complexity: O(n + max_rank * log(m * max_rank))
# space complexity: O(max_rank)
from math import floor
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars
        while left < right:
            time = left + (right - left) // 2
            repairCars = 0
            for rank in ranks:
                repairCars += floor((time / rank) ** 0.5)

            if repairCars >= cars:
                right = time
            else:
                left = time + 1

        return left


ranks = [4, 2, 3, 1]
cars = 10
print(Solution().repairCars(ranks, cars))
ranks = [5, 1, 8]
cars = 6
print(Solution().repairCars(ranks, cars))
