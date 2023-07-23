class Solution:
    def parseTernary(self, expression: str) -> str:
        if not expression:
            return ""
        validString = 'TF0123456789'

        def isValidAtomic(s: str):
            if s[0] not in 'TF':
                return False
            if s[1] != '?':
                return False
            if s[2] not in validString:
                return False
            if s[3] != ':':
                return False
            if s[4] not in validString:
                return False
            return True

        def solveAtomic(s: str):
            return s[2] if s[0] == 'T' else s[4]

        while len(expression) != 1:
            j = len(expression) - 1
            while not isValidAtomic(expression[j-4:j+1]):
                j -= 1
            expression = expression[:j-4] + \
                solveAtomic(expression[j-4:j+1]) + expression[j+1:]

        return expression