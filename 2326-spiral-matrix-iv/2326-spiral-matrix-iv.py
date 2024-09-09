# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        matrix = [[-1] * n for _ in range(m)]
        curr = head
        dirMap = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIdx = 0

        r, c = 0, 0

        while curr:
            matrix[r][c] = curr.val
            curr = curr.next

            dr, dc = dirMap[dirIdx]
            nextR, nextC = r + dr, c + dc

            if not (0 <= nextR < m and 0 <= nextC < n and matrix[nextR][nextC] == -1):
                dirIdx = (dirIdx + 1) % 4
                dr, dc = dirMap[dirIdx]
                nextR, nextC = r + dr, c + dc

            r, c = nextR, nextC

        return matrix


m = 3
n = 5
head = ListNode(3)
head.next = ListNode(0)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(8)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
print(Solution().spiralMatrix(m, n, head))
