# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        base = 9
        digits = 1
        while n > base * digits:
            n -= base * digits
            base *= 10
            digits += 1

        num = 10 ** (digits - 1) + (n - 1) // digits
        idx = (n - 1) % digits
        return int(str(num)[idx])
    
n = 3
print(Solution().findNthDigit(n))
