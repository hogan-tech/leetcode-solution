# time complexity: O(mnlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True
        ans = []
        for i in range(len(l)):
            arr = nums[l[i]: r[i] + 1]
            ans.append(check(arr))
        return ans


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
print(Solution().checkArithmeticSubarrays(nums, l, r))
