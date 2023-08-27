class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        nums = set()
        cur_num = 1

        while len(nums) < n:
            if cur_num not in nums and (target - cur_num) not in nums:
                nums.add(cur_num)
            cur_num += 1

        return sum(nums)


n = 2
target = 3
print(Solution().minimumPossibleSum(n, target))
