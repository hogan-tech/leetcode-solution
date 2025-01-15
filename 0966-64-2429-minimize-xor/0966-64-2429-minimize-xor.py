# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1

        targetSetBitsCount = bin(num2).count("1")
        setBitsCount = bin(result).count("1")

        currentBit = 0

        while setBitsCount < targetSetBitsCount:
            if not self.isSet(result, currentBit):
                result = self.setBit(result, currentBit)
                setBitsCount += 1
            currentBit += 1

        while setBitsCount > targetSetBitsCount:
            if self.isSet(result, currentBit):
                result = self.unsetBit(result, currentBit)
                setBitsCount -= 1
            currentBit += 1

        return result

    def isSet(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    def setBit(self, x: int, bit: int):
        return x | (1 << bit)

    def unsetBit(self, x: int, bit: int):
        return x & ~(1 << bit)


num1 = 3
num2 = 5
print(Solution().minimizeXor(num1, num2))
num1 = 1
num2 = 12
print(Solution().minimizeXor(num1, num2))
