# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for num, freq in Counter(nums).items():
            if freq == 2:
                result.append(num)
        return result


nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
print(Solution().getSneakyNumbers(nums))
