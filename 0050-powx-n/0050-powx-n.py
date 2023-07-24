class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            if abs(x) < 1e-6:
                raise ValueError("Cannot calculate power for x close to zero with negative n")
            result = 1.0
            x = 1 / x
            n = -n
            while n > 0:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
            return result
        else:
            result = 1.0
            while n > 0:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
            return result


x = 2.00000
n = -10
