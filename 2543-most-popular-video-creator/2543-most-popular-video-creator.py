# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creatorView = defaultdict(int)
        creatorPopularId = defaultdict(list)
        popularCreators = []
        maxView = -float('inf')
        for creator, id, view in zip(creators, ids, views):
            creatorView[creator] += view
            if creatorView[creator] > maxView:
                maxView = max(maxView, creatorView[creator])
            if creator in creatorPopularId:
                if view > creatorPopularId[creator][0]:
                    creatorPopularId[creator] = [view, id]
                if view == creatorPopularId[creator][0]:
                    if id < creatorPopularId[creator][1]:
                        creatorPopularId[creator] = [view, id]
            else:
                creatorPopularId[creator] = [view, id]
        for creator, totalView in creatorView.items():
            if totalView == maxView:
                popularCreators.append(creator)

        result = []
        for creator in popularCreators:
            result.append([creator, creatorPopularId[creator][1]])

        return result


creators = ["alice", "bob", "alice", "chris"]
ids = ["one", "two", "three", "four"]
views = [5, 10, 5, 4]
print(Solution().mostPopularCreator(creators, ids, views))
creators = ["alice", "alice", "alice"]
ids = ["a", "b", "c"]
views = [1, 2, 2]
print(Solution().mostPopularCreator(creators, ids, views))
creators = ["a"]
ids = ["a"]
views = [0]
print(Solution().mostPopularCreator(creators, ids, views))
