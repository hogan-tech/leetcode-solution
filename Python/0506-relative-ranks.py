# time complexity: O(n)
# space complexity: O(n)
import heapq
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

# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)

        # Create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))

        # Assign ranks to athletes
        rank = [0] * N
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place += 1

        return rank


score = [10, 3, 8, 9, 4]
print(Solution().findRelativeRanks(score))
