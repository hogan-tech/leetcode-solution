# time complexity: O(n)
# space complexity: O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        frequency = {}
        temp = head
        current = dummy.next
        prev = dummy

        while temp:
            if temp.val in frequency:
                frequency[temp.val] += 1
            else:
                frequency[temp.val] = 1
            temp = temp.next

        while current:
            if frequency[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(2)
print(Solution().deleteDuplicatesUnsorted(root))
