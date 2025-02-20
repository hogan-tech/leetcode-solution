# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        second = 0
        while second <= memory1 or second <= memory2:
            if memory2 > memory1:
                memory2 -= second
            else:
                memory1 -= second
            second += 1

        return [second, memory1, memory2]


memory1 = 2
memory2 = 2
print(Solution().memLeak(memory1, memory2))
memory1 = 8
memory2 = 11
print(Solution().memLeak(memory1, memory2))
memory1 = 6
memory2 = 4
print(Solution().memLeak(memory1, memory2))
