# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        numDict = {'1': '1', '0': '0', '8': '8', '6': '9', '9': '6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in numDict:
                return False
            if numDict[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


num = "69"
print(Solution().isStrobogrammatic(num))
num = "88"
print(Solution().isStrobogrammatic(num))
num = "2"
print(Solution().isStrobogrammatic(num))
