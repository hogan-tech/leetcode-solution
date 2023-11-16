# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)

nums = ["01", "10"]
print(Solution().findDifferentBinaryString(nums))
