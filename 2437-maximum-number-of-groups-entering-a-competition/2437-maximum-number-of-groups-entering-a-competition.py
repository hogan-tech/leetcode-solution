# time complexity: O(1)
# space complexity: O(1)
from math import sqrt
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int((sqrt(1 + 8 * len(grades)) - 1)/2)

'''
1:1
2:2 3
3:4 5 6
4:7 8 9 10
....
x:

(4 + 1) * (4) / 2 <= len(grades)

number of students: len(grades)
number of group: result = x

(x + 1) * (x) / 2 <= len(grades)

x^2 + x - 2len(grades) <= 0
a = 1
b = 1
c = -2len(grades)

(-b +- sqrt(b^2 - 4ac)) / 2a
(-b + sqrt(b^2 - 4ac)) / 2a


x = (-1 + sqrt(1 + 8 * len(grades))) // 2

'''
grades = [10, 6, 12, 7, 3, 5]
print(Solution().maximumGroups(grades))
grades = [8, 8]
print(Solution().maximumGroups(grades))
