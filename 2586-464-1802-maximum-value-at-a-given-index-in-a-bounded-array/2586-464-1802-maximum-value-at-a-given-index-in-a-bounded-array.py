# time complexity: O(log maxSum)
# space complexity: O(1)
class Solution:
    def getSum(self, index: int, mid: int, n: int) -> int:
        count = 0
        if mid > index:
            count += (mid + mid - index) * (index + 1)//2
        else:
            count += (mid + 1) * mid // 2 + index - mid + 1

        if mid >= n - index:
            count += (mid + mid - n + 1 + index) * (n - index) // 2
        else:
            count += (mid + 1) * mid // 2 + n - index - mid
        return count - mid

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left


n = 4
index = 2
maxSum = 6
print(Solution().maxValue(n, index, maxSum))
n = 6
index = 1
maxSum = 10
print(Solution().maxValue(n, index, maxSum))
