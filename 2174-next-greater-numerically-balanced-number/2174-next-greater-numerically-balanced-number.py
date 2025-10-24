# time complexity: O(C - n)
# space complexity: O(1)
from typing import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i


n = 1
print(Solution().nextBeautifulNumber(n))
n = 1000
print(Solution().nextBeautifulNumber(n))
n = 3000
print(Solution().nextBeautifulNumber(n))
