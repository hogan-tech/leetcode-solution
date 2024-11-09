# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = 0
        n -= 1
        binaryX = [0] * 64
        binaryN = [0] * 64

        for i in range(64):
            bit = (x >> i) & 1
            binaryX[i] = bit
            bit = (n >> i) & 1
            binaryN[i] = bit

        posX = 0
        posN = 0

        while posX < 63:
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        for i in range(64):
            if binaryX[i] == 1:
                result += pow(2, i)

        return result


n = 3000000000
x = 40000000122
print(Solution().minEnd(n, x))
