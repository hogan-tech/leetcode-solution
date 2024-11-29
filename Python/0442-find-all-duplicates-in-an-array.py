# time complexity: O(n)
# space complexity: O(1)
from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num, feq in Counter(nums).most_common():
            if feq > 1:
                ans.append(num)
        return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(nums))
