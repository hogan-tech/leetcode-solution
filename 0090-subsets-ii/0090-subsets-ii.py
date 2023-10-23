from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        hmap = Counter(nums)
        for key in hmap.keys():
            for i in range(0, len(powerset)):
                k = 0
                while (k < hmap[key]):
                    k += 1
                    powerset.append(list(powerset[i]+k*[key]))
        return powerset


nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))
