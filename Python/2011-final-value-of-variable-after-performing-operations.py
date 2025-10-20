# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if operation[0] == '+' or operation[-1] == '+':
                count += 1
            else:
                count -= 1
        return count


operations = ["--X", "X++", "X++"]
print(Solution().finalValueAfterOperations(operations))
operations = ["++X", "++X", "X++"]
print(Solution().finalValueAfterOperations(operations))
operations = ["X++", "++X", "--X", "X--"]
print(Solution().finalValueAfterOperations(operations))
