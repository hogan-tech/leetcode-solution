# time complexity: O(logn)
# space complexity: O(1)
def guess(mid: int) -> int:
    if mid > pick:
        return -1
    if mid < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            else:
                return mid
        return -1


n = 10
pick = 6
print(Solution().guessNumber(n))
