# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import defaultdict, deque
from typing import Dict, List


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def buildGraph(pairs: List[List[int]], rates: List[float]) -> Dict[str, List[tuple]]:
            graph = defaultdict(list)
            for (start, target), rate in zip(pairs, rates):
                graph[start].append((target, rate))
                graph[target].append((start, 1/rate))
            return graph

        def bfs(graph: Dict[str, List[tuple]], start: str, amount: float) -> Dict[str, float]:
            maxAmount = defaultdict(float)
            maxAmount[start] = amount
            q = deque()
            q.append((start, amount))

            while q:
                currCurrency, currAmount = q.popleft()
                for neighbor, rate in graph[currCurrency]:
                    temp = currAmount * rate
                    if temp > maxAmount[neighbor]:
                        maxAmount[neighbor] = temp
                        q.append((neighbor, temp))

            return maxAmount

        graph1 = buildGraph(pairs1, rates1)
        graph2 = buildGraph(pairs2, rates2)

        day1dict = bfs(graph1, initialCurrency, 1.0)

        result = 1.0
        for currency, amount in day1dict.items():
            day2dict = bfs(graph2, currency, amount)
            for targetCurrency, targetAmount in day2dict.items():
                if targetCurrency == initialCurrency:
                    result = max(result, targetAmount)
        return result


initialCurrency = "EUR"
pairs1 = [["EUR", "USD"], ["USD", "JPY"]]
rates1 = [2.0, 3.0]
pairs2 = [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]]
rates2 = [4.0, 5.0, 6.0]
print(Solution().maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2))

initialCurrency = "NGN"
pairs1 = [["NGN", "EUR"]]
rates1 = [9.0]
pairs2 = [["NGN", "EUR"]]
rates2 = [6.0]
print(Solution().maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2))

initialCurrency = "USD"
pairs1 = [["USD", "EUR"]]
rates1 = [1.0]
pairs2 = [["EUR", "JPY"]]
rates2 = [10.0]
print(Solution().maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2))
