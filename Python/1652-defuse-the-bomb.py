# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result
        for i in range(len(result)):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]
        return result


code = [5, 7, 1, 4]
k = 3
print(Solution().decrypt(code, k))
code = [1, 2, 3, 4]
k = 0
print(Solution().decrypt(code, k))
code = [2, 4, 9, 3]
k = -2
print(Solution().decrypt(code, k))
