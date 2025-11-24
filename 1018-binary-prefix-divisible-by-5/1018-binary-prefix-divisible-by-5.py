# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = list()
        prefix = 0
        for num in nums:
            prefix = ((prefix << 1) + num) % 5
            answer.append(prefix == 0)
        return answer


nums = [0, 1, 1]
print(Solution().prefixesDivBy5(nums))
nums = [1, 1, 1]
print(Solution().prefixesDivBy5(nums))
