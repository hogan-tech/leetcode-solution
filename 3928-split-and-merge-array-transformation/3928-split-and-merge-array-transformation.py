# time complexity: O(n^2)
# space complexity: O(n)
from typing import List
from collections import deque


class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        target = tuple(nums2)
        start = tuple(nums1)
        if start == target:
            return 0

        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)

        while queue:
            state, steps = queue.popleft()
            arr = list(state)
            if state == target:
                return steps
            for L in range(n):
                for R in range(L, n):
                    sub = arr[L:R+1]
                    left = arr[:L]
                    right = arr[R+1:]
                    remaining = left + right
                    k = len(remaining)
                    for pos in range(0, k+1):
                        newArr = remaining[:pos] + sub + remaining[pos:]
                        newState = tuple(newArr)
                        if newState not in visited:
                            visited.add(newState)
                            queue.append((newState, steps+1))
        return -1


nums1 = [3, 1, 2]
nums2 = [1, 2, 3]
print(Solution().minSplitMerge(nums1, nums2))
nums1 = [1, 1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1, 1]
print(Solution().minSplitMerge(nums1, nums2))
