# time complexity: O(min(klogk, mnlogmn))
# space complexity: O(min(k, mn))
from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        m = len(nums1)
        n = len(nums2)
        visited = set()
        visited.add((0, 0))
        heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        result = []
        while k:
            currVal, currIdx1, currIdx2 = heappop(minHeap)
            result.append([nums1[currIdx1], nums2[currIdx2]])
            if currIdx1+1 < m and (currIdx1+1, currIdx2) not in visited:
                heappush(minHeap, (nums1[currIdx1 + 1] +
                         nums2[currIdx2], currIdx1 + 1, currIdx2))
                visited.add((currIdx1+1, currIdx2))
            if currIdx2+1 < n and (currIdx1, currIdx2 + 1) not in visited:
                heappush(
                    minHeap, (nums1[currIdx1] + nums2[currIdx2 + 1], currIdx1, currIdx2 + 1))
                visited.add((currIdx1, currIdx2+1))
            k -= 1

        return result


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2
print(Solution().kSmallestPairs(nums1, nums2, k))
