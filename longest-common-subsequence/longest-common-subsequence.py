# time complexity: O(n*m)
# space compleixty: O(n*m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpGrid = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dpGrid[row][col] = 1 + dpGrid[row+1][col+1]
                else:
                    dpGrid[row][col] = max(
                        dpGrid[row+1][col], dpGrid[row][col+1])
        return dpGrid[0][0]


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
