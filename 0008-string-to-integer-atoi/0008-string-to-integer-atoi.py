import numpy as np


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        c = ' '
        i = 0
        while c == ' ' and i < n:
            c = s[i]
            i += 1
        i -= 1

        sgn = 1
        x = 0
        digit_len = 0
        c = s[i]
        if c == '-':
            sgn = -1
        elif c == '+':
            sgn = 1
        elif not np.char.isdigit(c):
            return 0
        else:
            x = ord(c)-ord('0')
            if x > 0:
                digit_len += 1
        i += 1

        while i < n and digit_len <= 12:
            c = s[i]
            if not np.char.isdigit(c):
                break
            x = 10*x+ord(c)-ord('0')
            i += 1
            if x > 0:
                digit_len += 1
        x = sgn*x

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if x > INT_MAX:
            x = INT_MAX
        elif x < INT_MIN:
            x = INT_MIN
        return x


S = "   -42"


print(Solution().myAtoi(S))
