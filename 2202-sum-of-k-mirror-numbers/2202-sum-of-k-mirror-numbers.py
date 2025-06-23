# time complexity: O(10 ^ 1/10)
# space complexity: O(1)
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, count, result = 1, 0, 0
        while count < n:
            right = left * 10
            for op in [0, 1]:
                for i in range(left, right):
                    if count == n:
                        break

                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        count += 1
                        result += combined
            left = right

        return result


k = 2
n = 5
print(Solution().kMirror(k, n))
k = 7
n = 17
print(Solution().kMirror(k, n))
