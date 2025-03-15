import re


class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        cellCol = ord(cell[0]) - ord('A')
        cellRow = int(cell[1:]) - 1
        self.sheet[cellRow][cellCol] = value

    def resetCell(self, cell: str) -> None:
        cellCol = ord(cell[0]) - ord('A')
        cellRow = int(cell[1:]) - 1
        self.sheet[cellRow][cellCol] = 0

    def getValue(self, formula: str) -> int:
        numsList = re.split(r"[=+]", formula)
        firstNum = numsList[1]
        secondNum = numsList[2]
        result = 0

        if firstNum.isdigit():
            result += int(firstNum)
        else:
            col = ord(firstNum[0]) - ord('A')
            row = int(firstNum[1:]) - 1
            result += self.sheet[row][col]

        if secondNum.isdigit():
            result += int(secondNum)
        else:
            col = ord(secondNum[0]) - ord('A')
            row = int(secondNum[1:]) - 1
            result += self.sheet[row][col]

        return result


'''
   A B C D ... X Y Z
1
2
.
.
10
'''

spreadsheet = Spreadsheet(3)
print(spreadsheet.getValue("=5+7"))
print(spreadsheet.setCell("A1", 10))
print(spreadsheet.getValue("=A1+6"))
print(spreadsheet.setCell("B2", 15))
print(spreadsheet.getValue("=A1+B2"))
print(spreadsheet.resetCell("A1"))
print(spreadsheet.getValue("=A1+B2"))
