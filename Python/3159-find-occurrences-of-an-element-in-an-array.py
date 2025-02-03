# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        freqDict = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if nums[i] == x:
                count += 1
                freqDict[count] = i

        result = []
        for query in queries:
            if query in freqDict:
                result.append(freqDict[query])
            else:
                result.append(-1)

        return result


nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
print(Solution().occurrencesOfElement(nums, queries, x))
nums = [1, 2, 3]
queries = [10]
x = 5
print(Solution().occurrencesOfElement(nums, queries, x))
