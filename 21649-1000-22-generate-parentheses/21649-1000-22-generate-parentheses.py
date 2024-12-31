# time complexity: O(4^n)
# space complexity: O(n)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(currString: str, leftCount: int, rightCount: int) -> None:
            if len(currString) == 2*n:
                result.append(currString)
                return
            if leftCount < n:
                backtrack(currString + "(", leftCount + 1, rightCount)
            if rightCount < leftCount:
                backtrack(currString + ")", leftCount, rightCount + 1)

        result = []
        backtrack("", 0, 0)
        return result


print(Solution().generateParenthesis(3))
