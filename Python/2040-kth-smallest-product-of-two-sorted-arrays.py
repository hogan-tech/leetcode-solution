# time complexity: O(nlogm * log(maxv))
# space complexity: O(1)
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        products = [nums1[0] * nums2[-1], nums1[0] * nums2[0], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        left, right = min(products), max(products)

        while left < right:
            mid = (left + right) // 2
            if self.countLessEqual(nums1, nums2, mid) >= k:  
                right = mid
            else:
                left = mid + 1
        return left
    
    def countLessEqual(self, nums1, nums2, mid):
        count = 0
        for i in nums1:
            if i < 0:  
                if nums2[0] * i <= mid:  
                    count += len(nums2)
                elif nums2[-1] * i > mid:  
                    continue
                else:  
                    l, r = 0, len(nums2) - 1
                    while l < r:
                        m = (l + r) // 2
                        if nums2[m] * i <= mid:
                            r = m
                        else:
                            l = m + 1
                    count += len(nums2) - l

            elif i > 0:  
                if nums2[-1] * i <= mid:  
                    count += len(nums2)
                elif nums2[0] * i > mid:  
                    continue
                else:  
                    l, r = 0, len(nums2) - 1
                    while l < r:
                        m = (l + r + 1) // 2
                        if nums2[m] * i <= mid:
                            l = m
                        else:
                            r = m - 1
                    count += l + 1

            else:  
                count += len(nums2) if mid >= 0 else 0

        return count



nums1 = [2,5]
nums2 = [3,4]
k = 2
print(Solution().kthSmallestProduct(nums1, nums2, k))
nums1 = [-4,-2,0,3]
nums2 = [2,4]
k = 6
print(Solution().kthSmallestProduct(nums1, nums2, k))
nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3
print(Solution().kthSmallestProduct(nums1, nums2, k))