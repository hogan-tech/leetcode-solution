# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        diffList = [(abs(num - median), num) for num in arr]
        diffList.sort(reverse=True)
        result = []
        for i in range(k):
            result.append(diffList[i][1])
        return result


arr = [6, -3, 7, 2, 11]
k = 3
print(Solution().getStrongest(arr, k))

arr = [1, 2, 3, 4, 5]
k = 2
print(Solution().getStrongest(arr, k))
arr = [1, 1, 3, 5, 5]
k = 2
print(Solution().getStrongest(arr, k))
arr = [6, 7, 11, 7, 6, 8]
k = 5
print(Solution().getStrongest(arr, k))
