# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        array.sort()
        if not array:
            return
        root = ListNode(array[0])
        current = root
        for i in range(1,len(array)):
            current.next = ListNode(array[i])
            current = current.next
        return root


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)


printLinkedList(Solution().sortList(root))
