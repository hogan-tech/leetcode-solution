from typing import DefaultDict, List


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flightMap = DefaultDict(list)
        self.result = []
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        for origin, itinerary in self.flightMap.items():
            itinerary.sort(reverse=True)

        self.DFS("JFK")

        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))
