# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        ans = 0
        if x >= 2**31 or x <= -2 ** 31:
            return 0
        if x > 0:
            ans = strX[::-1]
        if x < 0:
            temp = strX[1:]
            temp2 = temp[::-1]
            ans = "-" + temp2
        if int(ans) >= 2**31 - 1 or int(ans) <= -2 ** 31:
            return 0
        return int(ans)


x = -1230
print(Solution().reverse(x))
