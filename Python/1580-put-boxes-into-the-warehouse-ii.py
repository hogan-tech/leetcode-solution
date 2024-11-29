# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        left = result = 0
        right = len(warehouse) - 1
        for i in range(len(boxes)):
            if left <= right:
                if boxes[i] <= warehouse[left]:
                    left += 1
                    result += 1
                elif boxes[i] <= warehouse[right]:
                    right -= 1
                    result += 1
        return result


boxes = [1, 2, 2, 3, 4]
warehouse = [3, 4, 1, 2]
print(Solution().maxBoxesInWarehouse(boxes, warehouse))
