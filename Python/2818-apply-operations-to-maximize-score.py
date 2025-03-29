# time complexity: O(n * (sqrt(m) + logn))
# space complexity: O(n)
import heapq
import math
from typing import List


class Solution:
    MOD = 10**9 + 7

    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        primeScores = [0] * n

        for index in range(n):
            num = nums[index]
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    primeScores[index] += 1
                    while num % factor == 0:
                        num //= factor
            if num >= 2:
                primeScores[index] += 1

        next = [n] * n
        prev = [-1] * n

        monoStack = []

        for index in range(n):
            while (
                monoStack
                and primeScores[monoStack[-1]]
                < primeScores[index]
            ):
                topIdx = monoStack.pop()
                next[topIdx] = index

            if monoStack:
                prev[index] = monoStack[-1]

            monoStack.append(index)

        subArr = [0] * n
        for index in range(n):
            subArr[index] = (next[index] - index) * (
                index - prev[index]
            )

        pq = []
        for index in range(n):
            heapq.heappush(pq, (-nums[index], index))

        score = 1

        def power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    res = (res * base) % self.MOD
                base = (base * base) % self.MOD
                exponent //= 2
            return res

        while k > 0:
            num, index = heapq.heappop(pq)
            num = -num
            operations = min(k, subArr[index])
            score = (score * power(num, operations)) % self.MOD
            k -= operations

        return score


nums = [8, 3, 9, 3, 8]
k = 2
print(Solution().maximumScore(nums, k))
nums = [19, 12, 14, 6, 10, 18]
k = 3
print(Solution().maximumScore(nums, k))
