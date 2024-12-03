# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        spaces = spaces[::-1]
        for i, c in enumerate(s):
            if spaces and i == spaces[-1]:
                result += " "
                spaces.pop()
            result += c
        return result


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
print(Solution().addSpaces(s, spaces))
s = "icodeinpython"
spaces = [1, 5, 7, 9]
print(Solution().addSpaces(s, spaces))
s = "spacing"
spaces = [0, 1, 2, 3, 4, 5, 6]
print(Solution().addSpaces(s, spaces))
