# time complexity: O(m*n)
# space complexity: O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        N = len(num1) + len(num2)
        result = [0] * N

        firstNum = num1[::-1]
        secondNum = num2[::-1]

        for place1, digit1 in enumerate(firstNum):
            for place2, digit2 in enumerate(secondNum):
                currPos = place1 + place2

                carry = result[currPos]
                multiplication = int(digit1) * int(digit2) + carry

                result[currPos] = multiplication % 10

                result[currPos + 1] += multiplication // 10

        if result[-1] == 0:
            result.pop()

        return "".join(str(digit) for digit in result[::-1])


num1 = "2"
num2 = "3"
print(Solution().multiply(num1, num2))
num1 = "123"
num2 = "456"
print(Solution().multiply(num1, num2))
