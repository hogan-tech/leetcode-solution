# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(str(bin(i)).split("0b")[1].count('1'))
        return result


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for num in range(n + 1):
            if num % 2:
                result[num] = result[num // 2] + 1
            else:
                result[num] = result[num // 2]
        return result


print(Solution().countBits(5))
