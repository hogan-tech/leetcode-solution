# time complexity: O(nlogn)
# space complexity: O(n + s)
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankMap = {}
        sortedArr = sorted(arr)
        rank = 1
        for i in range(len(sortedArr)):
            if i > 0 and sortedArr[i] > sortedArr[i - 1]:
                rank += 1
            rankMap[sortedArr[i]] = rank
        for i in range(len(arr)):
            arr[i] = rankMap[arr[i]]
        return arr


arr = [40, 10, 20, 30]
print(Solution().arrayRankTransform(arr))
