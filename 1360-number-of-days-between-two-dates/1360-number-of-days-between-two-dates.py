from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        Y1, M1, D1 = map(int, date1.split("-"))
        Y2, M2, D2 = map(int, date2.split("-"))
        return abs((datetime(Y1, M1, D1) - datetime(Y2, M2, D2)).days)


date1 = "2019-06-29"
date2 = "2019-06-30"
print(Solution().daysBetweenDates(date1, date2))
