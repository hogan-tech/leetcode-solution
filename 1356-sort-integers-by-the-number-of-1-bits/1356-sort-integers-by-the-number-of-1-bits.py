from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(Solution().sortByBits(arr))
