# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rankScore = scores.copy()
        rankScore.sort(reverse=True)
        rankList = []
        for score in scores:
            rank = rankScore.index(score) + 1
            if 1 <= rank <= 3:
                rankList.append(medal[rank - 1])
            else:
                rankList.append(str(rank))
        return rankList


score = [10, 3, 8, 9, 4]
print(Solution().findRelativeRanks(score))
