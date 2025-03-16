# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        left = min(a, b, c)
        right = max(a, b, c)
        for num in [a, b, c]:
            if num != left and num != right:
                mid = num
        if left == mid - 1 and right == mid + 1:
            return [0, 0]
        if left == mid - 1 or right == mid + 1:
            return [1, right - left - 2]
        if left == mid - 2 or right == mid + 2:
            return [1, (right - mid - 1) + (mid - left - 1)]
        return [2, (right - mid - 1) + (mid - left - 1)]


'''
case 1: no move
return [0, 0]

case 2: one close, one move
return [1, right - left - 2]

case 3: 1 3 5
min = 5 -> 2
max = 5 -> 4, 1 -> 2

max = (right - mid - 1) + (mid - left - 1)

case 4: 1 4 7

'''

a = 1
b = 2
c = 5
print(Solution().numMovesStones(a, b, c))
a = 4
b = 3
c = 2
print(Solution().numMovesStones(a, b, c))
a = 3
b = 5
c = 1
print(Solution().numMovesStones(a, b, c))
a = 7
b = 4
c = 1
print(Solution().numMovesStones(a, b, c))
