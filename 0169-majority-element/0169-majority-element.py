# time complexity: O(n)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsSet = Counter(nums)
        return max(numsSet.keys(), key=numsSet.get)


Nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(Nums))
