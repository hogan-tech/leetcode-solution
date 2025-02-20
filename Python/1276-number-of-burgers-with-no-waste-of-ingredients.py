# time complexity: O(1)
# space complexity: O(1)
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]
        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = cheeseSlices - x
        return [int(x), int(y)] if (x >= 0 and y >= 0) and x == int(x) and y == int(y) else []


# Jumbo = X
# Small = Y
# 4X + 2Y = tomatoSlices
# X + Y = cheeseSlices
# X = (tomato - 2cheeseSlices) / 2
# y = cheeseSlices - X
# return [X, Y]

tomatoSlices = 16
cheeseSlices = 7
print(Solution().numOfBurgers(tomatoSlices, cheeseSlices))
tomatoSlices = 17
cheeseSlices = 4
print(Solution().numOfBurgers(tomatoSlices, cheeseSlices))
tomatoSlices = 4
cheeseSlices = 17
print(Solution().numOfBurgers(tomatoSlices, cheeseSlices))
tomatoSlices = 2
cheeseSlices = 1
print(Solution().numOfBurgers(tomatoSlices, cheeseSlices))
