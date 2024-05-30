from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for start in range(len(arr) - 1):
            xorA = 0
            for mid in range(start + 1, len(arr)):
                xorA ^= arr[mid-1]
                xorB = 0
                for end in range(mid, len(arr)):
                    xorB ^= arr[end]
                    if xorA == xorB:
                        ans += 1

        return ans


arr = [2, 3, 1, 6, 7]
print(Solution().countTriplets(arr))
