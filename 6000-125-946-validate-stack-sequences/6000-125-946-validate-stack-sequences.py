# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = deque(popped)
        for pushNum in pushed:
            stack.append(pushNum)

            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()

        return len(stack) == 0


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(Solution().validateStackSequences(pushed, popped))
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(Solution().validateStackSequences(pushed, popped))
