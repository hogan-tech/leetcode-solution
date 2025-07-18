# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        hp = [-x for x in nums[:n]]
        heapify(hp)
        part1[0] = total

        for i in range(n, n * 2):
            total += nums[i]
            heappush(hp, -nums[i])
            total -= -heappop(hp)
            part1[i - (n - 1)] = total

        part2 = sum(nums[n * 2:])
        hpR = nums[n * 2:]
        heapify(hpR)
        result = part1[n] - part2

        for i in range(n * 2 - 1, n - 1, -1):
            part2 += nums[i]
            heappush(hpR, nums[i])
            part2 -= heappop(hpR)
            result = min(result, part1[i - n] - part2)

        return result


nums = [3, 1, 2]
print(Solution().minimumDifference(nums))
nums = [7, 9, 5, 8, 1, 3]
print(Solution().minimumDifference(nums))
