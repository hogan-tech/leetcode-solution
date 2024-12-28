# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        outgoingNum = defaultdict(int)
        maxHeapSmall = []
        minHeapLarge = []
        for i in range(k):
            heappush(maxHeapSmall, -nums[i])
        for i in range(k // 2):
            heappush(minHeapLarge, -heappop(maxHeapSmall))

        balance = 0
        i = k
        while True:
            if k % 2:
                medians.append(float(-maxHeapSmall[0]))
            else:
                medians.append(
                    (minHeapLarge[0]-maxHeapSmall[0]) / 2.0)

            if i >= len(nums):
                break

            prevNum = nums[i-k]
            nextNum = nums[i]
            i += 1

            if prevNum <= -maxHeapSmall[0]:
                balance -= 1
            else:
                balance += 1

            if prevNum in outgoingNum:
                outgoingNum[prevNum] += 1
            else:
                outgoingNum[prevNum] = 1

            if maxHeapSmall and nextNum <= -maxHeapSmall[0]:
                balance += 1
                heappush(maxHeapSmall, -nextNum)
            else:
                balance -= 1
                heappush(minHeapLarge, nextNum)

            if balance < 0:
                heappush(maxHeapSmall, -minHeapLarge[0])
                heappop(minHeapLarge)
            elif balance > 0:
                heappush(minHeapLarge, -maxHeapSmall[0])
                heappop(maxHeapSmall)

            balance = 0

            while -maxHeapSmall[0] in outgoingNum and (outgoingNum[-maxHeapSmall[0]] > 0):
                outgoingNum[-maxHeapSmall[0]] -= 1
                heappop(maxHeapSmall)

            while minHeapLarge and minHeapLarge[0] in outgoingNum and (outgoingNum[minHeapLarge[0]] > 0):
                outgoingNum[minHeapLarge[0]] -= 1
                heappop(minHeapLarge)
        return medians


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().medianSlidingWindow(nums, k))
nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
k = 3
print(Solution().medianSlidingWindow(nums, k))
