# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        print(pairs)

        topKHeap = [x[0] for x in pairs[:k]]
        topKSum = sum(topKHeap)
        heapq.heapify(topKHeap)

        answer = topKSum * pairs[k-1][1]

        for i in range(k, len(nums1)):
            topKSum -= heapq.heappop(topKHeap)
            topKSum += pairs[i][0]
            heapq.heappush(topKHeap, pairs[i][0])

            answer = max(answer, topKSum*pairs[i][1])
        return answer


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
print(Solution().maxScore(nums1, nums2, k))
