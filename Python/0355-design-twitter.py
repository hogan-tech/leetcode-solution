from collections import defaultdict, deque
from typing import List


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for user, tweetId in self.feed if userId == user or user in self.follows[userId]][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
# [[],[1,1],[1],[2,1],[2],[2,1],[2]]
# obj = Twitter()
# obj.postTweet(1, 1)
# print(obj.getNewsFeed(1))
# obj.follow(2, 1)
# print(obj.getNewsFeed(2))
# obj.unfollow(2, 1)
# print(obj.getNewsFeed(2))


# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# obj = Twitter()
# obj.postTweet(1, 5)
# print(obj.getNewsFeed(1))
# obj.follow(1, 2)
# obj.postTweet(2, 6)
# print(obj.getNewsFeed(1))
# obj.unfollow(1, 2)
# print(obj.getNewsFeed(1))


# ["Twitter","getNewsFeed"]
# [[],[1]]
obj = Twitter()
obj.getNewsFeed(1)
