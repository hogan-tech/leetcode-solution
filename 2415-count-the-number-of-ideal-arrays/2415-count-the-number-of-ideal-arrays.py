# time complexity: O(n*maxValue*log(maxValue))
# space complexity: O(maxValue)
from math import comb
from typing import Counter


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue+1)}
        for k in range(1, n):
            temp = Counter()
            for x in freq:
                for m in range(2, maxValue//x+1):
                    ans += comb(n-1, k)*freq[x]
                    temp[m*x] += freq[x]
            freq = temp
            ans %= 10 ** 9+7
        return ans


n = 2
maxValue = 5
print(Solution().idealArrays(n, maxValue))
n = 5
maxValue = 3
print(Solution().idealArrays(n, maxValue))
