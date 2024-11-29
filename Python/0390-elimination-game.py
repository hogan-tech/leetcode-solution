# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remain = n
        head = 1
        step = 1
        while remain > 1:
            if left or remain % 2 == 1:
                head += step
            remain //= 2
            step *= 2
            left = not left

        return head


n = 24
print(Solution().lastRemaining(n))
n = 1
print(Solution().lastRemaining(n))