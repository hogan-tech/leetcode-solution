# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxList = [int(box) for box in boxes]
        result = []
        for i in range(n):
            temp = 0
            for j in range(n):
                temp += boxList[j] * abs(j-i)
            result.append(temp)
        return result


boxes = "110"
print(Solution().minOperations(boxes))
boxes = "001011"
print(Solution().minOperations(boxes))
