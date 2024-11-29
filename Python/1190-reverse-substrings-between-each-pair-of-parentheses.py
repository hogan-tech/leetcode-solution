# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        openParenthesesIndices = []
        pair = [0] * n
        for i in range(n):
            if s[i] == "(":
                openParenthesesIndices.append(i)
            if s[i] == ")":
                j = openParenthesesIndices.pop()
                pair[i] = j
                pair[j] = i
        result = []
        currIndex = 0
        direction = 1
        while currIndex < n:
            if s[currIndex] == "(" or s[currIndex] == ")":
                currIndex = pair[currIndex]
                direction = -direction
            else:
                result.append(s[currIndex])
            currIndex += direction
        return "".join(result)


s = "(abcd)"
print(Solution().reverseParentheses(s))
