class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        base = [i for i in range(1, n-1)] + [n-1, n-1]
        print(base)
        if sorted(nums) == sorted(base):
            return True
        else:
            return False