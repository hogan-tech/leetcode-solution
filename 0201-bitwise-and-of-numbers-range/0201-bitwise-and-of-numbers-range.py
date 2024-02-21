# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


left = 5
right = 7
print(Solution().rangeBitwiseAnd(left, right))
