# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sumDigit(num):
            return sum(int(d) for d in str(num))

        n = len(nums)
        sortedNums = sorted(nums, key=lambda n: (sumDigit(n), n))
        idxMap = {num: i for i, num in enumerate(sortedNums)}

        visited = [False] * n
        result = 0

        for i in range(n):
            if visited[i] or idxMap[nums[i]] == i:
                continue
            temp = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = idxMap[nums[j]]
                temp += 1
            if temp > 0:
                result += temp - 1
        return result


nums = [37, 100]
print(Solution().minSwaps(nums))
nums = [22, 14, 33, 7]
print(Solution().minSwaps(nums))
nums = [18, 43, 34, 16]
print(Solution().minSwaps(nums))
