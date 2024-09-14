# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        result = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                result.append(i)
        return result


height = [10, 1, 10, 1, 10]
threshold = 10
print(Solution().stableMountains(height, threshold))
