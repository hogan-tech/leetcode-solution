#time complexity: O(n)
#space complexity: O(1)

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxElement = max(arr)
        curr = arr[0]
        winCounting = 0
        for i in range(1, len(arr)):
            opponent = arr[i]
            if curr == maxElement:
                return curr
            if curr > opponent:
                winCounting += 1
            else:
                curr = opponent
                winCounting = 1
            if winCounting == k:
                return curr

        return curr


arr = [2, 1, 3, 5, 4, 6, 7]
k = 2

print(Solution().getWinner(arr, k))
