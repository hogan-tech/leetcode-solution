# time complexity: O(logk)
# space complexity: O(logk)
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1
        result = bin(k)[3:]
        result = result.replace('0', '4').replace('1', '7')
        return result


k = 4
print(Solution().kthLuckyNumber(k))
k = 10
print(Solution().kthLuckyNumber(k))
k = 1000
print(Solution().kthLuckyNumber(k))
