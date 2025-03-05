# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def alphabetBoardPath(self, target: str):
        size = 5
        curR, curC = 0, 0
        offset = ord('a')
        result = ''

        for c in target:
            row = (ord(c)-offset) // size
            col = (ord(c)-offset) % size
            print(row, col)
            if curR > col:
                result += 'L'*(curR-col)
            if row > curC:
                result += 'D'*(row-curC)
            if curC > row:
                result += 'U'*(curC-row)
            if col > curR:
                result += 'R'*(col-curR)

            result += '!'
            curR, curC = col, row

        return result


target = "leet"
print(Solution().alphabetBoardPath(target))
target = "code"
print(Solution().alphabetBoardPath(target))
target = "zdz"
print(Solution().alphabetBoardPath(target))
target = "gzz"
print(Solution().alphabetBoardPath(target))  # "DR!DDDLD!!"
