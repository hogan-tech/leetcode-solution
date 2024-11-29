# time complexity: O(n+m)
# space complexity: O(n+m)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        for _ in range(a - 1):
            current = current.next
        temp = current
        for _ in range(b - a + 2):
            temp = temp.next
        current.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = temp
        return list1


a = 3
b = 4

root1 = ListNode(10)
root1.next = ListNode(1)
root1.next.next = ListNode(13)
root1.next.next.next = ListNode(6)
root1.next.next.next.next = ListNode(9)
root1.next.next.next.next.next = ListNode(5)

root2 = ListNode(1000000)
root2.next = ListNode(1000001)
root2.next.next = ListNode(1000002)
print(Solution().mergeInBetween(root1, a, b, root2))
