# time complexity: O(max(n,m))
# space complexity: O(n)
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1 = set()
        for num in arr1:
            while num and num not in set1:
                set1.add(num)
                num = num // 10

        ans = -1
        for num in set(arr2):
            while num:
                if num in set1:
                    ans = max(ans, num)
                    break

                num = num // 10

        return 0 if ans == -1 else len(str(ans))


arr1 = [1, 10, 100]
arr2 = [1000]
print(Solution().longestCommonPrefix(arr1, arr2))
