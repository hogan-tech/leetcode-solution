class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return ans[::-1]


columnNumber = 28
print(Solution().convertToTitle(columnNumber))
