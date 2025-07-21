# time complexity: O(nlogm + n + qlogn)
# space complexity: O(n + q)
from typing import List


class SegmentTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
        self.size = size + 2

    def update(self, i, delta):
        i += 1
        while i < self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

    def rangeQuery(self, l, r):
        return self.query(r) - self.query(l - 1)


class Solution:
    def popcount_depth(self, x: int) -> int:
        depth = 0
        while x != 1:
            x = bin(x).count('1')
            depth += 1
        return depth

    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        maxK = 6

        depths = [self.popcount_depth(num) for num in nums]

        segTree = [SegmentTree(n) for _ in range(maxK)]
        for i, d in enumerate(depths):
            segTree[d].update(i, 1)

        result = []
        for query in queries:
            if query[0] == 1:
                _, l, r, k = query
                if k >= maxK:
                    result.append(0)
                else:
                    result.append(segTree[k].rangeQuery(l, r))
            else:
                _, idx, val = query
                oldDepth = depths[idx]
                newDepth = self.popcount_depth(val)
                if oldDepth < maxK:
                    segTree[oldDepth].update(idx, -1)
                if newDepth < maxK:
                    segTree[newDepth].update(idx, 1)
                nums[idx] = val
                depths[idx] = newDepth
        return result


nums = [2, 4]
queries = [[1, 0, 1, 1], [2, 1, 1], [1, 0, 1, 0]]
print(Solution().popcountDepth(nums, queries))
nums = [3, 5, 6]
queries = [[1, 0, 2, 2], [2, 1, 4], [1, 1, 2, 1], [1, 0, 1, 0]]
print(Solution().popcountDepth(nums, queries))
nums = [1, 2]
queries = [[1, 0, 1, 1], [2, 0, 3], [1, 0, 0, 1], [1, 0, 0, 2]]
print(Solution().popcountDepth(nums, queries))
