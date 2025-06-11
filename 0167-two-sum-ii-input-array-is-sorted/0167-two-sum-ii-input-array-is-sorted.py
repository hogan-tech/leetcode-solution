# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left + 1, right + 1]
            if currSum > target:
                right -= 1
            else:
                left += 1


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
numbers = [2, 3, 4]
target = 6
print(Solution().twoSum(numbers, target))
numbers = [-1, 0]
target = -1
print(Solution().twoSum(numbers, target))
