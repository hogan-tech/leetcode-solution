# time complexity: O(m+n)
# space complexity: O(m+n)
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
    
# time complexity: O(m+n)
# space complexity: O(m+n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx1 = 0
        idx2 = 0
        nums1.sort()
        nums2.sort()
        result = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return list(set(result))

# time complexity: O(m+n)
# space complexity: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []
        for num in nums1:
            seen[num] = 1
        
        for num in nums2:
            if num in seen:
                result.append(num)
                del seen[num]
        return result
            

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection(nums1, nums2))
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersection(nums1, nums2))
