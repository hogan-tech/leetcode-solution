# time complexity: O(nlogn + nlogw)
# space complexity: O(1)
from typing import List


class Solution:
    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        def countPairWithDistance(numbers: List[int], targetDistance: int):
            left = 0
            count = 0
            for right in range(1, len(numbers)):
                while numbers[right] - numbers[left] > targetDistance:
                    left += 1
                count += right - left
            return count

        numbers.sort()
        minDistance = 0
        maxDistance = numbers[-1] - numbers[0]
        while minDistance < maxDistance:
            midDistance = minDistance + (maxDistance - minDistance) // 2
            if countPairWithDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance

        return minDistance


nums = [1, 3, 1]
k = 1
print(Solution().smallestDistancePair(nums, k))
nums = [1, 1, 1]
k = 2
print(Solution().smallestDistancePair(nums, k))
nums = [1, 6, 1]
k = 3
print(Solution().smallestDistancePair(nums, k))
