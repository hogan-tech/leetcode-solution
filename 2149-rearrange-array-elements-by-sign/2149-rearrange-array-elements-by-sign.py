from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans


nums = [3, 1, -2, -5, 2, -4]
print(Solution().rearrangeArray(nums))
