from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for num in nums:
            if len(stack) % 2 == 0:
                stack.append(num)
            else:
                if stack[-1] == num:
                    count += 1
                else:
                    stack.append(num)
        return count + 1 if len(stack) % 2 else count


nums = [1, 1, 2, 3, 5]
print(Solution().minDeletion(nums))
nums = [1, 1, 2, 2, 3, 3]
print(Solution().minDeletion(nums))
