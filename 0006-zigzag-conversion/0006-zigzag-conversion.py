# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        backward = True
        i = 0
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                backward = not backward
            if backward:
                i -= 1
            else:
                i += 1
        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))
s = "A"
numRows = 1
print(Solution().convert(s, numRows))
