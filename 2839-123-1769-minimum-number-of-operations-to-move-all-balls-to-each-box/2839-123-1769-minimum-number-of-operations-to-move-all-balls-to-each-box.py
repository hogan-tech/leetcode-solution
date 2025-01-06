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

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        ballsToLeft = 0
        movesToLeft = 0
        ballsToRight = 0
        movesToRight = 0
        for i in range(n):
            answer[i] += movesToLeft
            ballsToLeft += int(boxes[i])
            movesToLeft += ballsToLeft

            j = n - 1 - i
            answer[j] += movesToRight
            ballsToRight += int(boxes[j])
            movesToRight += ballsToRight
        return answer


boxes = "110"
print(Solution().minOperations(boxes))
boxes = "001011"
print(Solution().minOperations(boxes))
