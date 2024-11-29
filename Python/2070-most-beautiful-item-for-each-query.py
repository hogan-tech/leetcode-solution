# time complexity: O((m+n)logm)
# space complexity: O(logm)
from typing import List


class Solution:
    def maximumBeauty(
        self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        # Sort and store max beauty
        items.sort(key=lambda x: x[0])

        maxBeauty = items[0][1]
        for i in range(len(items)):
            maxBeauty = max(maxBeauty, items[i][1])
            items[i][1] = maxBeauty
        return [self.binarySearch(items, q) for q in queries]

    def binarySearch(self, items, targetPrice):
        left, right = 0, len(items) - 1
        maxBeauty = 0
        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] > targetPrice:
                right = mid - 1
            else:
                maxBeauty = max(maxBeauty, items[mid][1])
                left = mid + 1
        return maxBeauty


items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries = [1, 2, 3, 4, 5, 6]
print(Solution().maximumBeauty(items, queries))

items = [[1, 2], [1, 2], [1, 3], [1, 4]]
queries = [1]
print(Solution().maximumBeauty(items, queries))

items = [[10, 1000]]
queries = [5]
print(Solution().maximumBeauty(items, queries))
