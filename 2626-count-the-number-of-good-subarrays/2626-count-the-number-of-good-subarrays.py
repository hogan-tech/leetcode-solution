# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = -1
        counter = defaultdict(int)
        sameCount = 0
        result = 0
        for left in range(len(nums)):
            while sameCount < k and right + 1 < n:
                right += 1
                sameCount += counter[nums[right]]
                counter[nums[right]] += 1
            if sameCount >= k:
                result += n - right

            counter[nums[left]] -= 1
            sameCount -= counter[nums[left]]

        return result


'''
x x
1
x x x
1 + 2
x x x x
1 + 2 + 3
x x x x x
1 + 2 + 3 + 4

n * (n - 1) // 2
'''

'''
1 1 1 1 1

0 1 3 6 10
'''
nums = [1, 1, 1, 1, 1]
k = 10
print(Solution().countGood(nums, k))
'''
3 1 4 3 2 2 4

0 0 0 1 1 2 3
'''
nums = [3, 1, 4, 3, 2, 2, 4]
k = 2
print(Solution().countGood(nums, k))
