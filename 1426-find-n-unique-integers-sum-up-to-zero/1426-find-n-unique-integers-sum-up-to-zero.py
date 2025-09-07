# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2:
            result = [-num for num in range(1, (n // 2) + 1)] + \
                [0] + [num for num in range(1, (n // 2) + 1)]
        else:
            result = [-num for num in range(1, (n // 2) + 1)] + \
                [num for num in range(1, (n // 2) + 1)]
        return result


'''
n = odd
(-n // 2) ~ -1 + 0 + 1 ~ n // 2
n = even
(-n // 2) ~ -1 + 1 ~ n // 2
'''

n = 5
print(Solution().sumZero(n))
n = 3
print(Solution().sumZero(n))
n = 1
print(Solution().sumZero(n))
n = 4
print(Solution().sumZero(n))
