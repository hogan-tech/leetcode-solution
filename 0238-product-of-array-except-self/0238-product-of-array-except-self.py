class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        Llist, Rlist, Ans = [0]*length, [0]*length, [0]*length

        Llist[0], Rlist[length - 1] = 1, 1
        for i in range(1, length):
            Llist[i] = Llist[i-1]*nums[i-1]

        for i in reversed(range(length-1)):
            Rlist[i] = Rlist[i+1]*nums[i+1]

        for i in range(length):
            Ans[i] = Llist[i] * Rlist[i]

        return Ans