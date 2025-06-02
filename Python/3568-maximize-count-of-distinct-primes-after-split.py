# time complexity: O((n + q) * log n)
# space complexity: O(n + U)
from typing import List
from collections import defaultdict
import heapq


class SegmentTree:
    def __init__(self, N: int):
        self.N = N
        self.size = 1
        while self.size < N:
            self.size <<= 1
        self.tree = [0] * (4 * N)
        self.lazy = [0] * (4 * N)

    def _apply(self, idx: int, left: int, right: int, val: int):
        self.tree[idx] += val
        self.lazy[idx] += val

    def _pushDown(self, idx: int, left: int, mid: int, right: int):
        if self.lazy[idx] != 0:
            self._apply(idx*2,   left,     mid, self.lazy[idx])
            self._apply(idx*2+1, mid+1, right, self.lazy[idx])
            self.lazy[idx] = 0

    def _updateRange(self, idx: int, left: int, right: int,
                     ql: int, qr: int, val: int):
        if ql > right or qr < left:
            return
        if ql <= left and right <= qr:
            self._apply(idx, left, right, val)
            return
        mid = (left + right) // 2
        self._pushDown(idx, left, mid, right)
        self._updateRange(idx*2,     left,   mid, ql, qr, val)
        self._updateRange(idx*2+1, mid+1, right, ql, qr, val)
        self.tree[idx] = max(self.tree[idx*2], self.tree[idx*2+1])

    def updateRange(self, l: int, r: int, val: int):
        if l > r:
            return
        self._updateRange(1, 1, self.N, l, r, val)

    def queryMax(self) -> int:
        return self.tree[1]


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        TOTAL = 10**5
        isPrime = [True] * (TOTAL+1)
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(TOTAL**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, TOTAL+1, i):
                    isPrime[j] = False

        positions = defaultdict(set)
        minHp = defaultdict(list)
        maxHp = defaultdict(list)

        def getLeft(p):
            h = minHp[p]
            s = positions[p]

            while h and h[0] not in s:
                heapq.heappop(h)
            return h[0] if h else None

        def getRight(p):
            h = maxHp[p]
            s = positions[p]
            while h and -h[0] not in s:
                heapq.heappop(h)
            return -h[0] if h else None

        for i, v in enumerate(nums):
            if v <= TOTAL and isPrime[v]:
                positions[v].add(i)
                heapq.heappush(minHp[v], i)
                heapq.heappush(maxHp[v], -i)

        if n-1 >= 1:
            segTree = SegmentTree(n-1)
        else:
            segTree = SegmentTree(1)
        for p, idxSet in positions.items():
            if not idxSet:
                continue
            L = getLeft(p)
            R = getRight(p)
            if L is not None and L+1 <= n-1:
                segTree.updateRange(L+1, n-1,  1)
            if R is not None and R >= 1:
                segTree.updateRange(1, min(R, n-1), 1)

        result = []

        for idx, newVal in queries:
            oldVal = nums[idx]

            if oldVal <= TOTAL and isPrime[oldVal]:
                p = oldVal
                prevLeft = getLeft(p)
                prevRight = getRight(p)

                positions[p].remove(idx)

                if not positions[p]:
                    if prevLeft is not None and prevLeft+1 <= n-1:
                        segTree.updateRange(prevLeft+1, n-1, -1)
                    if prevRight is not None and prevRight >= 1:
                        segTree.updateRange(1, min(prevRight, n-1), -1)

                    minHp[p].clear()
                    maxHp[p].clear()
                else:
                    nextLeft = getLeft(p)
                    nextRight = getRight(p)

                    if idx == prevLeft:
                        if prevLeft+1 <= nextLeft:
                            segTree.updateRange(prevLeft+1, nextLeft, -1)

                    if idx == prevRight:
                        if nextRight+1 <= prevRight:
                            segTree.updateRange(nextRight+1, prevRight, -1)

            nums[idx] = newVal
            if newVal <= TOTAL and isPrime[newVal]:
                p = newVal
                empty = (not positions[p])
                if empty:
                    if idx+1 <= n-1:
                        segTree.updateRange(idx+1, n-1, +1)
                    if idx >= 1:
                        segTree.updateRange(1, idx, +1)

                    positions[p].add(idx)
                    heapq.heappush(minHp[p], idx)
                    heapq.heappush(maxHp[p], -idx)

                else:

                    prevLeft = getLeft(p)
                    prevRight = getRight(p)

                    positions[p].add(idx)
                    heapq.heappush(minHp[p], idx)
                    heapq.heappush(maxHp[p], -idx)

                    nextLeft = getLeft(p)
                    nextRight = getRight(p)
                    if nextLeft < prevLeft:
                        if nextLeft+1 <= prevLeft:
                            segTree.updateRange(nextLeft+1, prevLeft, +1)

                    if nextRight > prevRight:
                        low = prevRight + 1
                        high = min(nextRight, n-1)
                        if low <= high:
                            segTree.updateRange(low, high, +1)

            result.append(segTree.queryMax())

        return result


nums = [2, 1, 3, 1, 2]
queries = [[1, 2], [3, 3]]
print(Solution().maximumCount(nums, queries))
nums = [2, 1, 4]
queries = [[0, 1]]
print(Solution().maximumCount(nums, queries))
