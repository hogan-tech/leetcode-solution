# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def findComplement(self, num: int) -> int:
        bit = 1
        while num >= bit:
            num ^= bit
            bit <<= 1
        return num

num = 5
print(Solution().findComplement(num))
