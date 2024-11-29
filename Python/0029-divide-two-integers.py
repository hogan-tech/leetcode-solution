# time complexity: O(1)
# space complexity: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend >= 0 and divisor <
                      0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minusLimit = -(2**31)
        plusLimit = (2**31 - 1)
        result = min(max(result, minusLimit), plusLimit)
        return result


dividend = 7
divisor = -3
print(Solution().divide(dividend, divisor))
