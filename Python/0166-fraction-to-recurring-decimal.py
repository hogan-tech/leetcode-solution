# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        fraction = []
        if (numerator < 0) != (denominator < 0):
            fraction.append('-')
        dividend = abs(numerator)
        divisor = abs(denominator)

        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append('.')
        lookup = {}
        while remainder != 0:
            print(remainder)
            if remainder in lookup:
                fraction.insert(lookup[remainder], '(')
                fraction.append(')')
                break

            lookup[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        print(lookup)

        return "".join(fraction)


numerator = 4
denominator = 333
print(Solution().fractionToDecimal(numerator, denominator))
