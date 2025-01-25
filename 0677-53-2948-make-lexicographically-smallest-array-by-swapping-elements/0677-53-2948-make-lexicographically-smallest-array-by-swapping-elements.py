# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict, deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        numsSorted = sorted(nums)

        currGroup = 0
        numToGroup = defaultdict(int)
        numToGroup[numsSorted[0]] = currGroup

        groupToList = defaultdict(deque)
        groupToList[currGroup].append(numsSorted[0])
        
        for i in range(1, len(numsSorted)):
            if abs(numsSorted[i] - numsSorted[i - 1]) > limit:
                currGroup += 1
            numToGroup[numsSorted[i]] = currGroup
            groupToList[currGroup].append(numsSorted[i])
            
        for i in range(len(nums)):
            group = numToGroup[nums[i]]
            nums[i] = groupToList[group].popleft()
            

        return nums


nums = [1, 5, 3, 9, 8]
limit = 2
print(Solution().lexicographicallySmallestArray(nums, limit))
nums = [1, 7, 6, 18, 2, 1]
limit = 3
print(Solution().lexicographicallySmallestArray(nums, limit))
nums = [1, 7, 28, 19, 10]
limit = 3
print(Solution().lexicographicallySmallestArray(nums, limit))
