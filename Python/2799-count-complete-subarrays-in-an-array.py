# time complexity: O(n)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctCount = len(set(nums))
        count = 0
        left = 0
        right = 0
        counter = Counter()
        n = len(nums)
        while right < n:
            counter[nums[right]] += 1
            while len(counter) == distinctCount:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                count += n - right
            right += 1

        return count


nums = [1, 3, 1, 2, 2]
print(Solution().countCompleteSubarrays(nums))
nums = [5, 5, 5, 5]
print(Solution().countCompleteSubarrays(nums))
