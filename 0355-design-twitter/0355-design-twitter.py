# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.time = 1
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = list(self.users[userId])
        for user in self.followers[userId]:
            news.extend(self.users[user])
        news.sort(reverse=True, key=lambda x: x[0])
        result = []
        for i in range(len(news)):
            if i == 10:
                break
            result.append(news[i][1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
# [[],[1,1],[1],[2,1],[2],[2,1],[2]]
obj1 = Twitter()
obj1.postTweet(1, 1)
print(obj1.getNewsFeed(1))
obj1.follow(2, 1)
print(obj1.getNewsFeed(2))
obj1.unfollow(2, 1)
print(obj1.getNewsFeed(2))


# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
obj2 = Twitter()
obj2.postTweet(1, 5)
print(obj2.getNewsFeed(1))
obj2.follow(1, 2)
obj2.postTweet(2, 6)
print(obj2.getNewsFeed(1))
obj2.unfollow(1, 2)
print(obj2.getNewsFeed(1))


# ["Twitter","getNewsFeed"]
# [[],[1]]
obj3 = Twitter()
obj3.getNewsFeed(1)
