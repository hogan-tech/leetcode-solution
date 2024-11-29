# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = len(arr)//4
        count = 0
        temp = arr[0]
        for i in range(len(arr)):
            if temp == arr[i]:
                count += 1
            else:
                count = 1
            if count > freq:
                return arr[i]
            temp = arr[i]
        return 0


arr = [1, 2, 3, 3]
print(Solution().findSpecialInteger(arr))
