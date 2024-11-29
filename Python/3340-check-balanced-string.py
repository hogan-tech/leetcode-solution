# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        for i in range(len(num)):
            if i % 2:
                odd += int(num[i])
            else:
                even += int(num[i])
        return odd == even


num = "1234"
print(Solution().isBalanced(num))
