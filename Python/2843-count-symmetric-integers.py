class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def checkSymmetric(numStr):
            digitList = [int(digit) for digit in numStr]
            n = len(digitList) // 2
            return sum(digitList[:n]) == sum(digitList[n:])

        result = 0
        for num in range(low, high + 1):
            num = str(num)
            if len(num) % 2:
                continue
            if checkSymmetric(num):
                result += 1
                
        return result


low = 1
high = 100
print(Solution().countSymmetricIntegers(low, high))
low = 1200
high = 1230
print(Solution().countSymmetricIntegers(low, high))
