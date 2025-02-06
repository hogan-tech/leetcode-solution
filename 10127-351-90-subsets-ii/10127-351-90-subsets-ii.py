# time complexit: O(2^n + nlogn)
# space complexity: O(n)
from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start: int, comb: List[int], counter: Counter):
            if list(comb) not in result:
                result.append(list(comb))
            for i in range(start, len(nums)):
                if counter[nums[i]] > 0:
                    counter[nums[i]] -= 1
                    comb.append(nums[i])
                    backtrack(i + 1, comb, counter)
                    comb.pop()
                    counter[nums[i]] += 1

        backtrack(0, [], Counter(nums))
        return result


nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))
