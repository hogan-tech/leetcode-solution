# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        counts = [[0] * 27 for _ in range(26)]
        for t in range(26):
            counts[t][26] = chr(ord('A') + t)

        for i in range(len(votes)):
            for j, c in enumerate(votes[i]):
                counts[ord(c) - ord('A')][j] -= 1

        counts.sort()
        result = ""
        for i in range(len(votes[0])):
            result += counts[i][26]

        return result


votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
print(Solution().rankTeams(votes))
votes = ["WXYZ", "XYZW"]
print(Solution().rankTeams(votes))
votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
print(Solution().rankTeams(votes))
