# time complexity: O(n)
# space complexity: O(log(min(a,b)))
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))
        for i in range(0, len(nums), 2):
            currNum = int(nums[i])
            currDenom = int(nums[i + 1])
            num = num * currDenom + currNum * denom
            denom = denom * currDenom
        gcd = abs(self.findGcd(num, denom))
        num //= gcd
        denom //= gcd
        return str(num) + "/" + str(denom)

    def findGcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self.findGcd(b % a, a)


expression = "-1/2+1/2"
print(Solution().fractionAddition(expression))
