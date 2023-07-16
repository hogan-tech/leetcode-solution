class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        numsLen = len(nums)
        sum = 0
        for i in range(1,numsLen+1):
            if(numsLen % i == 0):
                sum += nums[i-1]**2
        return sum