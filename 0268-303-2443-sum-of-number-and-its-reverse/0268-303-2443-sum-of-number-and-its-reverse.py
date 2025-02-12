# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num // 2, num + 1):
            str1 = str(i)
            str2 = str1[::-1]
            if int(str1) + int(str2) == num:
                return True
        return False


num = 443
print(Solution().sumOfNumberAndReverse(num))
num = 63
print(Solution().sumOfNumberAndReverse(num))
num = 181
print(Solution().sumOfNumberAndReverse(num))
