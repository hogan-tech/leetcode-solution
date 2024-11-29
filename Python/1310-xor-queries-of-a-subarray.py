# time complexity: O(n+q)
# space complexity: O(n)
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorList = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            xorList[i + 1] = xorList[i] ^ arr[i]
        return [xorList[left] ^ xorList[right+1] for left, right in queries]


arr = [4, 8, 2, 10]
queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
print(Solution().xorQueries(arr, queries))
