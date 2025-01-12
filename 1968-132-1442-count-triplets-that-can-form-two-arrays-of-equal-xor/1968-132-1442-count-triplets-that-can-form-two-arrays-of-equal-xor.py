# time complexity: O(n^3)
# space complexity: O(1)
from collections import defaultdict
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

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        prefix = 0
        countMap = defaultdict(int, {0: 1})
        totalMap = defaultdict(int)
        for i in range(len(arr)):
            prefix ^= arr[i]
            count += countMap[prefix] * i - totalMap[prefix]
            countMap[prefix] += 1
            totalMap[prefix] += i + 1
        return count


arr = [2, 3, 1, 6, 7]
print(Solution().countTriplets(arr))
arr = [1, 1, 1, 1, 1]
print(Solution().countTriplets(arr))
