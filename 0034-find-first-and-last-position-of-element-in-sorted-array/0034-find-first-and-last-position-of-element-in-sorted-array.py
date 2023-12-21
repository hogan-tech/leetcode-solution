from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        upper_bound = self.findBound(nums, target, False)
        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                if isFirst:
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(Solution().searchRange(nums, target))
