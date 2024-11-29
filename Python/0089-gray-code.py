# time complexity: O(n*2^n)
# space complexity: O(2^n)
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        visited = {0}
        self.backtracking(result, n, visited)
        return result

    def backtracking(self, result: List[int], n: int, visited: dict):
        if len(result) == (1 << n):
            return True
        current = result[-1]
        for i in range(n):
            nextNum = current ^ (1 << i)
            if nextNum not in visited:
                visited.add(nextNum)
                result.append(nextNum)
                if self.backtracking(result, n, visited):
                    return True
                visited.remove(nextNum)
                result.pop()
        return False


n = 2
print(Solution().grayCode(n))
