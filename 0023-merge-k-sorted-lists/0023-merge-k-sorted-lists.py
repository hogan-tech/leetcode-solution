# time complexity: O(nlogn)
# space complexity: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeList = []
        for node in lists:
            while node:
                nodeList.append(node.val)
                node = node.next

        dummy = curr = ListNode()
        for num in sorted(nodeList):
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next