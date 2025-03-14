# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checkValid(amount):
            child = 0
            for candy in candies:
                child += candy // amount
                if child >= k:
                    return True
            return False

        right = max(candies)
        left = 0
        while left < right:
            mid = left + (right - left + 1) // 2
            if checkValid(mid):
                left = mid
            else:
                right = mid - 1

        if not checkValid(1):
            return 0
        return left


'''
1 2 3 4 5 6 7 8 9 10
l       m          r
'''

candies = [1, 2, 3, 4, 10]
k = 5
print(Solution().maximumCandies(candies, k))
candies = [5, 8, 6]
k = 3
print(Solution().maximumCandies(candies, k))
candies = [2, 5]
k = 11
print(Solution().maximumCandies(candies, k))
