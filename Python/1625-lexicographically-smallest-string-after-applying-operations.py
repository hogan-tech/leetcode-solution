# time complexity: O(n*10^n)
# space complexity: O(10^n)
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result = [s]
        visit = set()

        def backtrack(s, add, rotate):
            if s in visit:
                return
            visit.add(s)
            temp = ''
            for i in range(len(s)):
                if i % 2:
                    temp += str((int(s[i]) + add) % 10)
                else:
                    temp += s[i]
            if temp < result[0]:
                result[0] = temp
            backtrack(temp, add, rotate)
            s = s[rotate:] + s[:rotate]
            if s < result[0]:
                result[0] = s
            backtrack(s, add, rotate)
            return

        backtrack(s, a, b)
        return result[0]


s = "5525"
a = 9
b = 2
print(Solution().findLexSmallestString(s, a, b))
s = "74"
a = 5
b = 1
print(Solution().findLexSmallestString(s, a, b))
s = "0011"
a = 4
b = 2
print(Solution().findLexSmallestString(s, a, b))
