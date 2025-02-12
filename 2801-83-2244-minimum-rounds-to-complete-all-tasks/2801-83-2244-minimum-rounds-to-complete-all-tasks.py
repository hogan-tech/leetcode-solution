# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = 0
        for value in Counter(tasks).values():
            if value == 1:
                return -1
            remain = value % 3
            count += value // 3 + (1 if remain else 0)
        return count


# 5 -> 3 2
# 9 -> 3
# 10 -> 3 ... 1 + 1 -> 3 3 2 2
# 11 -> 3 ... 2 + 1
# 12 -> 4
tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
print(Solution().minimumRounds(tasks))
tasks = [2, 3, 3]
print(Solution().minimumRounds(tasks))
