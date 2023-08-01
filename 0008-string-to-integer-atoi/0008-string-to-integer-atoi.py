class Solution:
    def myAtoi(self, s: str) -> int:
        x = ""
        y = ""
        start = 0
        nums = "0123456789"
        for i in range(len(s)):
            if s[i] != " ":
                start = i
                break
        for i in range(start, len(s)):
            if s[i] in "-+":
                if x == "" and y == "":
                    x = s[i]
                else:
                    break
            elif s[i] in nums:
                y += s[i]
            else:
                break

        if y == "":
            return 0
        if x == "-":
            if int(y) > 2**31:
                return -2**31
            else:
                return -int(y)
        else:
            if int(y) > 2**31-1:
                return 2**31-1
            else:
                return int(y)


