# time complexity: O(elog(e/v))
# space complexity: O(v+e)
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        result = []
        for u, v in tickets:
            adjList[u].append(v)
        
        for flights in adjList.values():
            flights.sort(reverse = True)

        def dfs(original):
            nonlocal result
            while adjList[original]:
                nextFlight = adjList[original].pop()
                dfs(nextFlight)
            result.append(original)

        dfs('JFK')
        return result[::-1]

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))
tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(Solution().findItinerary(tickets))
