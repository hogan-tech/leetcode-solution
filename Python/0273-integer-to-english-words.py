class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        lessTwentyMap = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                         "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tensMap = ["", "", "Twenty", "Thirty", "Forty",
                   "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousandsMap = ["", "Thousand", "Million", "Billion"]

        def helper(num: int):
            if num == 0:
                return ""
            elif num < 20:
                return lessTwentyMap[num] + " "
            elif num < 100:
                return tensMap[num // 10] + " " + helper(num % 10)
            else:
                return lessTwentyMap[num // 100] + " Hundred " + helper(num % 100)

        result = ""
        for i, unit in enumerate(thousandsMap):
            if num % 1000 != 0:
                result = helper(num % 1000) + unit + " " + result
            num //= 1000
        return result.strip()


num = 1234567
print(Solution().numberToWords(num))
