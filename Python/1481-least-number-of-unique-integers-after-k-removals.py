# time complexity: O(nlogn)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrFeq = list(Counter(arr).values())
        arrFeq.sort()
        removed = 0
        for i in range(len(arrFeq)):
            removed += arrFeq[i]
            if removed > k:
                return len(arrFeq) - i
        return 0


arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(Solution().findLeastNumOfUniqueInts(arr, k))
