# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def concatHex36(self, n: int) -> str:
        def Base36(num: int) -> str:
            if num == 0:
                return '0'

            chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            result = ''

            while num > 0:
                num, remain = divmod(num, 36)
                result = chars[remain] + result

            return result

        return hex(n**2)[2:].upper() + Base36(n**3)


n = 13
print(Solution().concatHex36(n))
n = 36
print(Solution().concatHex36(n))
