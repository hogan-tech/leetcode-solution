class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            return hex(2**32 + num)[2:]
        else:
            return hex(num)[2:]


num = 26
print(Solution().toHex(num))
num = -1
print(Solution().toHex(num))
