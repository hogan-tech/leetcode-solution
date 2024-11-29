# time complexity: O(logk ^ 2)
# space complexity: O(1)
class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1
        kthLuckyNum = ""
        while k > 1:
            kthLuckyNum = "".join((("7" if k & 1 else "4"), kthLuckyNum))
            k >>= 1
        return kthLuckyNum


k = 10
print(Solution().kthLuckyNumber(k))
