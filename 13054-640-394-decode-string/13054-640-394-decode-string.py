# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        current = ""
        countStack = []
        stringStack = []
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                countStack.append(k)
                stringStack.append(current)
                k = 0
                current = ""
            elif c == ']':
                prevString = stringStack.pop()
                prevNum = countStack.pop()
                current = prevString + current * prevNum
            else:
                current += c

        return current


s = "3[a]2[bc]"
print(Solution().decodeString(s))
s = "3[a2[c]]"
print(Solution().decodeString(s))
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))
