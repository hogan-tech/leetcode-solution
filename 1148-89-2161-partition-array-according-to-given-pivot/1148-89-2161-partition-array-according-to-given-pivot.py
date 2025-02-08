# time compelxtiy: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        count = 0
        for num in nums:
            if num < pivot:
                result.append(num)
            if num == pivot:
                count += 1

        result.extend([pivot] * count)

        for num in nums:
            if num > pivot:
                result.append(num)

        return result


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
print(Solution().pivotArray(nums, pivot))
nums = [-3, 4, 3, 2]
pivot = 2
print(Solution().pivotArray(nums, pivot))
