# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        for num in order:
            if num in friends:
                result.append(num)
        return result


order = [3, 1, 2, 5, 4]
friends = [1, 3, 4]
print(Solution().recoverOrder(order, friends))
order = [1, 4, 5, 3, 2]
friends = [2, 5]
print(Solution().recoverOrder(order, friends))
