# time complexity: O(2^n)
# space complexity: O(n)
import math


class Solution(object):
    def numSquares(self, n):
        squareNums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(i):
            if i in squareNums:
                return 1
            minNum = float('inf')

            for square in squareNums:
                if i < square:
                    break
                minNum = min(minNum, minNumSquares(i - square) + 1)
            return minNum

        return minNumSquares(n)

# time complexity: O(n*n^0.5)
# space complexity: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        squareNums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squareNums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]


# time complexity: O(n^(h/2)) h is the maximal number of recursion that could happen.
# space complexity: O(n^0.5)
class Solution:
    def numSquares(self, n):

        def isDividedBy(n, count):
            if count == 1:
                return n in squareNums
            for i in squareNums:
                if isDividedBy(n - i, count - 1):
                    return True
            return False

        squareNums = set([i * i for i in range(1, math.sqrt(n) + 1)])
        for count in range(1, n+1):
            if isDividedBy(n, count):
                return count

# time complexity: O(n^(h/2)) h is the maximal number of recursion that could happen.
# space complexity: O(n^(1/h))
class Solution:
    def numSquares(self, n):
        squareNums = [i * i for i in range(1, math.sqrt(n) + 1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            nextQueue = set()
            for remainder in queue:
                for squareNum in squareNums:    
                    if remainder == squareNum:
                        return level  
                    elif remainder < squareNum:
                        break
                    else:
                        nextQueue.add(remainder - squareNum)
            queue = nextQueue
        return level
    

# time complexity: O(n^(0.5))
# space complexity: O(1)
class Solution:
    def isSquare(self, n: int) -> bool:
        square = int(math.sqrt(n))
        return square*square == n

    def numSquares(self, n: int) -> int:
        while (n & 3) == 0:
            n >>= 2     
        if (n & 7) == 7: 
            return 4

        if self.isSquare(n):
            return 1
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        return 3

n = 12
print(Solution().numSquares(n))
n = 13
print(Solution().numSquares(n))
