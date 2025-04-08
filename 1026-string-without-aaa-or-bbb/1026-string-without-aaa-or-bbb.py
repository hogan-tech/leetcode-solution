# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = ""
        while a or b:
            if result[-2:] == 'aa':
                result += 'b'
                b -= 1
            elif result[-2:] == 'bb':
                result += 'a'
                a -= 1
            elif a > b:
                result += 'a'
                a -= 1
            else:
                result += 'b'
                b -= 1

        return result


a = 1
b = 2
print(Solution().strWithout3a3b(a, b))
a = 4
b = 1
print(Solution().strWithout3a3b(a, b))
