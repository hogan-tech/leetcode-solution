# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        backward = True
        index = 0
        for char in s:
            rows[index] += char
            if index == 0 or index == numRows - 1:
                backward = not backward
            if backward:
                index -= 1
            else:
                index += 1
        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
