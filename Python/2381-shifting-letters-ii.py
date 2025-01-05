# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        operation = [0] * n
        for start, end, direction in shifts:
            if direction:
                operation[start] += 1
                if end + 1 < n:
                    operation[end + 1] -= 1
            else:
                operation[start] -= 1
                if end + 1 < n:
                    operation[end + 1] += 1

        prefix = [0] * n
        prefix[0] = operation[0]
        for i in range(1, n):
            prefix[i] = operation[i] + prefix[i-1]

        result = ""
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            result += chr((curr + prefix[i]) % 26 + ord('a'))
        return result


s = "abxka"
shifts = [[2, 3, 1], [0, 2, 0], [1, 4, 0]]
print(Solution().shiftingLetters(s, shifts))
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(Solution().shiftingLetters(s, shifts))
s = "dztz"
shifts = [[0, 0, 0], [1, 1, 1]]
print(Solution().shiftingLetters(s, shifts))
