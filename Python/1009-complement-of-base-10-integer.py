# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bitCount = n.bit_length()
        bitMask = (1 << bitCount) - 1
        return n ^ bitMask


n = 5
print(Solution().bitwiseComplement(n))
n = 7
print(Solution().bitwiseComplement(n))
n = 10
print(Solution().bitwiseComplement(n))
