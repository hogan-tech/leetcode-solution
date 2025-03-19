# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution(object):
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = left = 0
        while left < n:
            right = left
            if right + 1 < n and arr[right] < arr[right + 1]:
                while right+1 < n and arr[right] < arr[right+1]:
                    right += 1
                if right + 1 < n and arr[right] > arr[right + 1]:
                    while right+1 < n and arr[right] > arr[right+1]:
                        right += 1
                    result = max(result, right - left + 1)
            left = max(right, left + 1)
        return result


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().longestMountain(arr))
'''
0 1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 5 4 2 1  0
l
'''
arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
print(Solution().longestMountain(arr))
'''
0 1 2 3 4 5 6

2 1 4 7 3 2 5
          l
            m
            r
'''
arr = [2, 1, 4, 7, 3, 2, 5]
print(Solution().longestMountain(arr))
'''
2 2 2
l
m
r
'''
arr = [2, 2, 2]
print(Solution().longestMountain(arr))
