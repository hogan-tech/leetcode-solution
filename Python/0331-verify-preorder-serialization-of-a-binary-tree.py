# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(Solution().isValidSerialization(preorder))
preorder = "1,#"
print(Solution().isValidSerialization(preorder))
preorder = "9,#,#,1"
print(Solution().isValidSerialization(preorder))
