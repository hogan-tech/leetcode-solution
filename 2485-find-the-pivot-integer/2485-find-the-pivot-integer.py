# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        total = n * (n + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if mid * mid - total < 0:
                left = mid + 1
            else:
                right = mid
        if left * left - total == 0:
            return left
        return -1

n = 8
print(Solution().pivotInteger(n))
