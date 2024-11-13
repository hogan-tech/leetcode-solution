from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(curString: str, leftCount: int, rightCount: int) -> None:
            if len(curString) == 2 * n:
                ans.append(curString)
                return
            if leftCount < n:
                backtracking(curString + "(", leftCount + 1, rightCount)
            if rightCount < leftCount:
                backtracking(curString + ")", leftCount, rightCount + 1)

        ans = []
        backtracking("", 0, 0)
        return ans


print(Solution().generateParenthesis(1))