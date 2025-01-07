# time complexity: O(elog(e/v))
# space complexity: O(v+e)
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.flightMap = defaultdict(list)
        self.result = []
        for origin, dest in tickets:
            self.flightMap[origin].append(dest)
        for origin, itinerary in self.flightMap.items():
            itinerary.sort(reverse=True)

        self.dfs('JFK')
        return self.result[::-1]
    
    def dfs(self, original: str):
        destList = self.flightMap[original]
        while destList:
            nextDest = destList.pop()
            self.dfs(nextDest)
        self.result.append(original)

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))
tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(Solution().findItinerary(tickets))
