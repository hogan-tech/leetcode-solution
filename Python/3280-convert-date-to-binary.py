class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dateList = date.split('-')
        result = ""
        for item in dateList:
            result += bin(int(item))[2:] + '-'
        return result[:-1]

date = "1900-01-01"
print(Solution().convertDateToBinary(date))