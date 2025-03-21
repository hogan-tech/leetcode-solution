# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        flag = False
        for i, c in enumerate(num):
            currInt = int(c)
            if currInt < change[currInt]:
                flag = True
                num[i] = str(change[currInt])
            elif currInt > change[currInt] and flag:
                break

        return ''.join(num)


num = "132"
change = [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]
print(Solution().maximumNumber(num, change))
num = "021"
change = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]
print(Solution().maximumNumber(num, change))
num = "5"
change = [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]
print(Solution().maximumNumber(num, change))
