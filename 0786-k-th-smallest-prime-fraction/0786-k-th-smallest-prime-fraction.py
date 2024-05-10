from itertools import combinations
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arrList, fractionList = [], []
        for item in combinations(arr, 2):
            arrList.append(item)
            fractionList.append(item[0]/item[1])
        fractionList, arrList = zip(
            *sorted(zip(fractionList, arrList), key=lambda x: x[0]))
        return list(arrList[k-1])


arr = [1, 2, 3, 5]
k = 3
print(Solution().kthSmallestPrimeFraction(arr, k))
