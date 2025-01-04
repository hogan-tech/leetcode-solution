# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        remainTarget = target
        for i, num in enumerate(arr):
            if remainTarget <= num * (n - i):
                replacementValue = remainTarget / (n - i)
                if replacementValue - int(replacementValue) == 0.5:
                    return int(replacementValue)
                return round(replacementValue)
            remainTarget -= num
        return arr[-1]


arr = [4, 9, 3]
target = 10
print(Solution().findBestValue(arr, target))
arr = [2, 3, 5]
target = 10
print(Solution().findBestValue(arr, target))
arr = [60864, 25176, 27249, 21296, 20204]
target = 56803
print(Solution().findBestValue(arr, target))
