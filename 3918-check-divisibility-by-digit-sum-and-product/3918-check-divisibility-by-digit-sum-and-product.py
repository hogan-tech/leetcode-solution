# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        numList = [int(num) for num in str(n)]
        digitSum = sum(numList)
        digitProduct = 1
        for num in numList:
            digitProduct *= num
        total = digitSum + digitProduct
        return n % total == 0


n = 99
print(Solution().checkDivisibility(n))
n = 23
print(Solution().checkDivisibility(n))
