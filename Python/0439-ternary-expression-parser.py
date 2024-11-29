class Solution:
    def parseTernary(self, expression: str) -> str:
        if not expression:
            return ''

        validChars = 'TF0123456789'

        def isValidAtomic(s: str):
            return len(s) >= 5 and s[0] in 'TF' and s[1] == '?' and s[2] in validChars and s[3] == ':' and s[4] in validChars

        def solveAtomic(s: str):
            return s[2] if s[0] == 'T' else s[4]

        while len(expression) != 1:
            j = len(expression) - 1
            while not isValidAtomic(expression[j-4:j+1]):
                j -= 1
            expression = expression[:j-4] + \
                solveAtomic(expression[j-4:j+1]) + expression[j+1:]

        return expression


Expression = 'F?1:T?4:5'

