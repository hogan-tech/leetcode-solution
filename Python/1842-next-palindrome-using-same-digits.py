# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def nextPalindrome(self, num: str) -> str:
        def findNextPermutation(digits):
            i = len(digits) - 2
            while i >= 0 and digits[i] >= digits[i+1]:
                i -= 1
            if i == -1:
                return False
            j = len(digits) - 1
            while digits[j] <= digits[i]:
                j -= 1
            digits[i], digits[j] = digits[j], digits[i]
            digits[i+1:] = reversed(digits[i+1:])
            return True

        n = len(num)
        if n == 1:
            return ""
        midLen = n // 2
        leftHalf = list(num[:midLen])

        if not findNextPermutation(leftHalf):
            return ""

        if n % 2 == 0:
            nextPalidrome = ''.join(leftHalf + leftHalf[::-1])
        else:
            midDigit = num[midLen]
            nextPalidrome = ''.join(leftHalf + [midDigit] + leftHalf[::-1])

        if nextPalidrome > num:
            return nextPalidrome
        return ""


num = "1221"
print(Solution().nextPalindrome(num))
num = "32123"
print(Solution().nextPalindrome(num))
num = "45544554"
print(Solution().nextPalindrome(num))
