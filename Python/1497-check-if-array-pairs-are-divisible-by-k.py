# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for x in arr:
            cnt[x % k] += 1

        if (cnt[0] % 2):
            return False
        for i in range(1, k // 2 + k % 2):
            if (cnt[i] != cnt[k-i]):
                return False
        return True


arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
print(Solution().canArrange(arr, k))
