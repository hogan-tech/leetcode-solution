# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        firstHalfEnd = self.endOfFirstHalf(head)
        secondHalfStart = self.reverseList(firstHalfEnd.next)

        result = True
        firstPos = head
        seconfPos = secondHalfStart
        while result and seconfPos:
            if firstPos.val != seconfPos.val:
                result = False
            firstPos = firstPos.next
            seconfPos = seconfPos.next
        firstHalfEnd.next = self.reverseList(secondHalfStart)
        return result

    def endOfFirstHalf(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

# time complexity: O(n)
# space complexity: O(n)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindromList = []
        while head:
            palindromList.append(head.val)
            head = head.next
        i = 0
        j = len(palindromList) - 1
        while i < j:
            if palindromList[i] != palindromList[j]:
                return False
            i += 1
            j -= 1
        return True


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(2)
root.next.next.next = ListNode(1)
print(Solution().isPalindrome(root))
