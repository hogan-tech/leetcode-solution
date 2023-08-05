# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            temp = ListNode(self.gcd(node.next.val, node.val))
            temp.next = node.next
            node.next = temp
            node = node.next.next
        return head