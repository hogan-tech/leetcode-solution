from itertools import permutations
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums == sorted(nums, key=lambda x: -x):
            nums.sort()
            return

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                minIdx, minVal = len(nums), float('inf')
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1] and nums[j] < minVal:
                        minVal = nums[j]
                        minIdx = j
                nums[i - 1], nums[minIdx] = nums[minIdx], nums[i - 1]

                while True:
                    swapped = False
                    for k in range(i, len(nums) - 1):
                        if nums[k] > nums[k + 1]:
                            swapped = True
                            nums[k], nums[k + 1] = nums[k + 1], nums[k]
                    if swapped == False:
                        break

                return


nums = [1, 2, 3]
print(Solution().nextPermutation(nums))
