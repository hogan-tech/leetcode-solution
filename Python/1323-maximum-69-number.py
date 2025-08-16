# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maximum69Number(self, num: int) -> int:
        original = list(str(num))
        for i, digit in enumerate(original):
            if digit == '6':
                original[i] = '9'
                break
        return int(''.join(original))


num = 9669
print(Solution().maximum69Number(num))
num = 9996
print(Solution().maximum69Number(num))
num = 9999
print(Solution().maximum69Number(num))