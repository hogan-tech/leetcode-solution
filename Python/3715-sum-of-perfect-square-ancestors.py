# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
from collections import defaultdict

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        maxLen = 10**5
        smallPrimeFactor = list(range(maxLen + 1))
        for i in range(2, int(maxLen**0.5) + 1):
            if smallPrimeFactor[i] == i:
                for j in range(i * i, maxLen + 1, i):
                    if smallPrimeFactor[j] == j:
                        smallPrimeFactor[j] = i

        def squareFree(x: int) -> int:
            result = 1
            while x > 1:
                p = smallPrimeFactor[x]
                count = 0
                while x % p == 0:
                    x //= p
                    count ^= 1
                if count == 1:
                    result *= p
            return result

        squareNums = [squareFree(num) for num in nums]

        freq = defaultdict(int)
        result = 0

        def dfs(node: int, parent: int):
            nonlocal result
            squareFree = squareNums[node]
            result += freq[squareFree]
            freq[squareFree] += 1
            for neighbor in adjList[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
            freq[squareFree] -= 1

        dfs(0, -1)
        return result


n = 3
edges = [[0, 1], [1, 2]]
nums = [2, 8, 2]
print(Solution().sumOfAncestors(n, edges, nums))
n = 3
edges = [[0, 1], [0, 2]]
nums = [1, 2, 4]
print(Solution().sumOfAncestors(n, edges, nums))
n = 4
edges = [[0, 1], [0, 2], [1, 3]]
nums = [1, 2, 9, 4]
print(Solution().sumOfAncestors(n, edges, nums))
