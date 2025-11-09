# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            if num2 > num1:
                num2 -= num1
            else:
                num1 -= num2
            count += 1
        return count


num1 = 2
num2 = 3
print(Solution().countOperations(num1, num2))
num1 = 10
num2 = 10
print(Solution().countOperations(num1, num2))
