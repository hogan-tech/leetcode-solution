# time complexity: O(n + mlogm)
# space complexity: O(m)
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        result = 0
        while total > 0:
            total -= capacity[result]
            result += 1

        return result


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(Solution().minimumBoxes(apple, capacity))
apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(Solution().minimumBoxes(apple, capacity))
