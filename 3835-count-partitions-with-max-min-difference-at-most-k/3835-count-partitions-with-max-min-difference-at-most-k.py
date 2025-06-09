# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n+1)
        prefix = [0] * (n+1)

        dp[0] = 1
        prefix[0] = 1

        queueMax = deque()
        queueMin = deque()

        count = 0
        for i in range(1, n+1):
            while queueMax and nums[queueMax[-1]] <= nums[i-1]:
                queueMax.pop()
            queueMax.append(i-1)

            while queueMin and nums[queueMin[-1]] >= nums[i-1]:
                queueMin.pop()
            queueMin.append(i-1)

            while nums[queueMax[0]] - nums[queueMin[0]] > k:
                if queueMax[0] == count:
                    queueMax.popleft()
                if queueMin[0] == count:
                    queueMin.popleft()
                count += 1

            dp[i] = (prefix[i-1] - (prefix[count-1] if count > 0 else 0)) % MOD
            prefix[i] = (prefix[i-1] + dp[i]) % MOD

        return dp[n]


nums = [9, 4, 1, 3, 7]
k = 4
print(Solution().countPartitions(nums, k))
nums = [3, 3, 4]
k = 0
print(Solution().countPartitions(nums, k))
