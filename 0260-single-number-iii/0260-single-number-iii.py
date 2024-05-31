from typing import Counter, List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for key, val in Counter(nums).items():
            if val == 1:
                result.append(key)
        return result


nums = [1, 2, 1, 3, 2, 5]
print(Solution().singleNumber(nums))
