# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        bitList = ['0'] * 32
        binString = bin(n)[2:]
        length = len(binString)
        for i in range(32 - length, 32):
            bitList[i] = binString[i - 32 + length]

        resultBin = "".join(bitList)[::-1]
        return int(resultBin, 2)


n = 43261596
print(Solution().reverseBits(n))
n = 4294967293
print(Solution().reverseBits(n))
