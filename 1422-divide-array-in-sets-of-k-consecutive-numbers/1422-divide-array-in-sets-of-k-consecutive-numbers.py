# time complexity: O(n*k)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()

        freq = defaultdict(int)
        if len(nums) % k != 0:
            return False
        for num in nums:
            freq[num] += 1

        for num in nums:
            if freq[num] > 0:
                for curr in range(num, num + k):
                    if freq[curr] == 0:
                        return False
                    freq[curr] -= 1
        return True


nums = [1, 2, 3, 3, 4, 4, 5, 6]
k = 4
print(Solution().isPossibleDivide(nums, k))
nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3
print(Solution().isPossibleDivide(nums, k))
nums = [1, 2, 3, 4]
k = 3
print(Solution().isPossibleDivide(nums, k))
