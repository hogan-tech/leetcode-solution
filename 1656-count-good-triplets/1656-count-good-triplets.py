# time complexity: O(n^3)
# space complexity: O(1)
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    I = arr[i]
                    J = arr[j]
                    K = arr[k]
                    if abs(I - J) <= a and abs(J-K) <= b and abs(K-I) <= c:
                        result += 1
        return result


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(Solution().countGoodTriplets(arr, a, b, c))
arr = [1, 1, 2, 2, 3]
a = 0
b = 0
c = 1
print(Solution().countGoodTriplets(arr, a, b, c))
