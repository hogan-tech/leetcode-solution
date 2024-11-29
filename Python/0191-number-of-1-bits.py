# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


n = 11111111111111111111111111111101
print(Solution().hammingWeight(n))
