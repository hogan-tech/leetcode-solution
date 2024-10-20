from typing import List


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def calculate(TFList: List[bool], operation: str) -> bool:
            if operation == "|":
                temp = TFList[0]
                for item in TFList:
                    temp |= item
                return temp
            if operation == "!":
                return not TFList[0]
            if operation == "&":
                temp = TFList[0]
                for item in TFList:
                    temp &= item
                return temp
            
        operationStack = []
        boolStack = []
        for char in expression:
            if char in ["&", "!", "|"]:
                operationStack.append(char)
            if char in ["f", "t", "(", ")"]:
                if char == "f":
                    boolStack.append(False)
                if char == "t":
                    boolStack.append(True)
                if char == "(":
                    boolStack.append("(")
                if char == ")":
                    tempTFList = []
                    while boolStack:
                        temp = boolStack.pop()
                        if temp == "(":
                            break
                        else:
                            tempTFList.append(temp)
                    boolStack.append(calculate(tempTFList, operationStack.pop()))
        return boolStack[0]


expression = "&(|(f))"
print(Solution().parseBoolExpr(expression))
expression = "|(f,f,f,t)"
print(Solution().parseBoolExpr(expression))
expression = "!(&(f,t))"
print(Solution().parseBoolExpr(expression))
expression = "&(t,t,t)"
print(Solution().parseBoolExpr(expression))