# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for c in s:
            if c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            elif c == '*':
                result = result[:-1]
            else:
                result += c

        return result


s = "a#b%*"
print(Solution().processStr(s))
s = "z*#"
print(Solution().processStr(s))
s = "*aaa*"
print(Solution().processStr(s))
