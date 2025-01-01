# time complexity: O(nl)
# space complexity: O(l)
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def leftShift(s: str, num: int):
            return s[num:] + s[:num]

        def rightShift(s: str, num: int):
            return s[-num:] + s[:-num]

        for direction, num in shift:
            num %= len(s)
            if direction:
                s = rightShift(s, num)
            else:
                s = leftShift(s, num)
        return s


s = "abc"
shift = [[0, 1], [1, 2]]
print(Solution().stringShift(s, shift))
s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
print(Solution().stringShift(s, shift))
s = "abc"
shift = [[0, 4]]
print(Solution().stringShift(s, shift))
