# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        arr = []
        for i, (num1, num2) in enumerate(zip(nums1, nums2)):
            arr.append([num1, num2, i])
        arr.sort()
        result = [0] * len(nums1)
        minHp = []
        sumHp = 0

        j = 0
        for num1, num2, i in arr:
            while j < len(arr) and arr[j][0] < num1:
                heappush(minHp, arr[j][1])
                sumHp += arr[j][1]
                if len(minHp) > k:
                    sumHp -= heappop(minHp)
                j += 1
            result[i] = sumHp if len(minHp) > 0 else 0
        return result


'''
result[2] = 0
result[1] = 30
result[4] = 30 + 20
result[0] = 30 + 50
result[3] = 30 + 50
'''

nums1 = [4, 2, 1, 5, 3]
nums2 = [10, 20, 30, 40, 50]
k = 2
print(Solution().findMaxSum(nums1, nums2, k))
nums1 = [2, 2, 2, 2]
nums2 = [3, 1, 2, 3]
k = 1
print(Solution().findMaxSum(nums1, nums2, k))
