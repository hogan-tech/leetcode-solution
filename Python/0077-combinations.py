from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        baseList = []
        result = []
        for i in range(1, n+1):
            baseList.append(i)
        baseList = list(combinations(baseList, k))
        for i, item in enumerate(baseList):
            result.append(list(item))
        return result