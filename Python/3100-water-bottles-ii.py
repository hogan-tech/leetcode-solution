# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottle = 0
        bottleDrunk = 0
        while fullBottles > 0 or emptyBottle >= numExchange:
            if fullBottles > 0:
                emptyBottle += fullBottles
                bottleDrunk += fullBottles
                fullBottles = 0
            if emptyBottle >= numExchange:
                emptyBottle -= numExchange
                fullBottles += 1
                numExchange += 1
        return bottleDrunk


numBottles = 13
numExchange = 6
print(Solution().maxBottlesDrunk(numBottles, numExchange))
numBottles = 10
numExchange = 3
print(Solution().maxBottlesDrunk(numBottles, numExchange))
