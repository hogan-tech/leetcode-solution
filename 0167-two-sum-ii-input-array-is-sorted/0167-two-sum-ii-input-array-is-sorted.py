from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if target - numbers[left] < numbers[right]:
                right -= 1
                continue
            if target - numbers[left] == numbers[right]:
                return [left+1, right+1]
            left += 1
        return []


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
