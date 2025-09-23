# time complexity: O(n+m+max(n,m))
# space complexity: O(n+m)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


version1 = "1.01"
version2 = "1.001"
print(Solution().compareVersion(version1, version2))
