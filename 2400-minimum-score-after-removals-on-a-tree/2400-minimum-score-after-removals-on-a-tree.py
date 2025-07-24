# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        total = 0
        for num in nums:
            total ^= num

        result = float("inf")

        def dfs2(x: int, f: int, oth: int, anc: int) -> int:
            son = nums[x]
            for y in adj[x]:
                if y == f:
                    continue
                son ^= dfs2(y, x, oth, anc)
            if f == anc:
                return son
            nonlocal result
            result = min(result, self.calc(oth, son, total ^ oth ^ son))
            return son

        def dfs(x: int, f: int) -> int:
            son = nums[x]
            for y in adj[x]:
                if y == f:
                    continue
                son ^= dfs(y, x)
            for y in adj[x]:
                if y == f:
                    dfs2(y, x, son, x)
            return son

        dfs(0, -1)
        return result


nums = [1, 5, 5, 4, 11]
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
print(Solution().minimumScore(nums, edges))
nums = [5, 5, 2, 4, 4, 2]
edges = [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]
print(Solution().minimumScore(nums, edges))
