# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = -1 if num < 0 else 1
        num = str(abs(num))
        digits = []
        for c in num:
            digits.append(c)
        if sign < 0:
            digits.sort(reverse=True)
        else:
            digits.sort()
            for i, c in enumerate(digits):
                if c != '0':
                    digits[i], digits[0] = digits[0], digits[i]
                    break

        result = int(''.join(digits)) * sign
        return result


num = 310
print(Solution().smallestNumber(num))
num = -7605
print(Solution().smallestNumber(num))
