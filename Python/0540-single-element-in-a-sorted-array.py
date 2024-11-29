from collections import Counter
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for item in list(Counter(nums).items()):
            if(item[1] == 1):
                return item[0]
        return 0
    


nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))