# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


num1 = 12
num2 = 5
print(Solution().sum(num1, num2))
num1 = -10
num2 = 4
print(Solution().sum(num1, num2))
