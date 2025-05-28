# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]


num = 23
print(Solution().encode(num))
num = 107
print(Solution().encode(num))
