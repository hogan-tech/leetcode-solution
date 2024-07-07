class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles // numExchange >= 1:
            remains = numBottles % numExchange
            total += numBottles // numExchange
            numBottles = numBottles // numExchange + remains
        return total


numBottles = 9
numExchange = 3
print(Solution().numWaterBottles(numBottles, numExchange))
