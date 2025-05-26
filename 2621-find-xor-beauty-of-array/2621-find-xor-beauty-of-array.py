from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        binaryList = [0] * 32
        for num in nums:
            for i, bint in enumerate(reversed(bin(num)[2:])):
                binaryList[i] += int(bint)
        binaryList = [str(num % 2) for num in binaryList]
        return int("".join(binaryList[::-1]), 2)


'''
- (0,0,0) with effective value ((1 | 1) & 1) = 1
- (0,0,1) with effective value ((1 | 1) & 4) = 0
- (0,1,0) with effective value ((1 | 4) & 1) = 1
- (0,1,1) with effective value ((1 | 4) & 4) = 4
- (1,0,0) with effective value ((4 | 1) & 1) = 1
- (1,0,1) with effective value ((4 | 1) & 4) = 4
- (1,1,0) with effective value ((4 | 4) & 1) = 0
- (1,1,1) with effective value ((4 | 4) & 4) = 4 

1 = 0001
4 = 0100

(0001 | 0001) & 0001 = 0001 -> (i, i, i) = num[i]

15 = 001111
45 = 101101
20 = 010100
02 = 000010
34 = 100010
35 = 100011
05 = 000101
44 = 101100
32 = 100000
30 = 011110



34 = 100010

'''
nums = [1, 4]
print(Solution().xorBeauty(nums))
nums = [15, 45, 20, 2, 34, 35, 5, 44, 32, 30]
print(Solution().xorBeauty(nums))
