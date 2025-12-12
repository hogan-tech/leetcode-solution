# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        onlineUsers = set(range(numberOfUsers))
        offlineUsers = {}

        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        for event in events:
            eventType, timestamp, data = event
            timestamp = int(timestamp)

            usersToRestore = [
                uid for uid, returnTime in offlineUsers.items() if returnTime <= timestamp]
            for uid in usersToRestore:
                onlineUsers.add(uid)
                del offlineUsers[uid]

            if eventType == "OFFLINE":
                userId = int(data)
                onlineUsers.discard(userId)
                offlineUsers[userId] = timestamp + 60

            elif eventType == "MESSAGE":
                mentionedUsers = data.split()

                if "ALL" in mentionedUsers:
                    for user in range(numberOfUsers):
                        mentions[user] += 1

                elif "HERE" in mentionedUsers:
                    for user in onlineUsers:
                        mentions[user] += 1

                else:
                    for userStr in mentionedUsers:
                        if userStr.startswith("id"):
                            userId = int(userStr[2:])
                            mentions[userId] += 1

        return mentions


numberOfUsers = 2
events = [["MESSAGE", "10", "id1 id0"], [
    "OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]
print(Solution().countMentions(numberOfUsers, events))
numberOfUsers = 2
events = [["MESSAGE", "10", "id1 id0"], [
    "OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]
print(Solution().countMentions(numberOfUsers, events))
numberOfUsers = 2
events = [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]
print(Solution().countMentions(numberOfUsers, events))
numberOfUsers = 3
events = [["MESSAGE", "2", "HERE"], ["OFFLINE", "2", "1"],
          ["OFFLINE", "1", "0"], ["MESSAGE", "61", "HERE"]]
# expect = [1,0,2]
print(Solution().countMentions(numberOfUsers, events))
