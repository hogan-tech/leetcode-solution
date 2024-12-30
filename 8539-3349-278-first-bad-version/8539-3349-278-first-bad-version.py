# time complexity: O(logn)
# space complexity: O(1)
def isBadVersion(version: int) -> bool:
    if version == bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


n = 5
bad = 4
print(Solution().firstBadVersion(n))
n = 1
bad = 1
print(Solution().firstBadVersion(n))
