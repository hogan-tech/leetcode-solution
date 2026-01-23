# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Node:
    def __init__(self, value, left):
        self.value = value
        self.left = left
        self.prev = None
        self.next = None


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        class PQItem:
            def __init__(self, first, second, cost):
                self.first = first
                self.second = second
                self.cost = cost

            def __lt__(self, other):
                if self.cost == other.cost:
                    return self.first.left < other.first.left
                return self.cost < other.cost

        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        decreaseCount = 0
        count = 0

        for i in range(1, len(nums)):
            newNode = Node(nums[i], i)
            current.next = newNode
            newNode.prev = current
            heapq.heappush(
                pq, PQItem(current, newNode, current.value + newNode.value)
            )

            if nums[i - 1] > nums[i]:
                decreaseCount += 1

            current = newNode

        while decreaseCount > 0:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if (
                merged[first.left]
                or merged[second.left]
                or first.value + second.value != cost
            ):
                continue
            count += 1

            if first.value > second.value:
                decreaseCount -= 1

            prevNode = first.prev
            nextNode = second.next
            first.next = nextNode
            if nextNode:
                nextNode.prev = first

            if prevNode:
                if prevNode.value > first.value and prevNode.value <= cost:
                    decreaseCount -= 1
                elif prevNode.value <= first.value and prevNode.value > cost:
                    decreaseCount += 1

                heapq.heappush(
                    pq, PQItem(prevNode, first, prevNode.value + cost)
                )

            if nextNode:
                if second.value > nextNode.value and cost <= nextNode.value:
                    decreaseCount -= 1
                elif second.value <= nextNode.value and cost > nextNode.value:
                    decreaseCount += 1
                heapq.heappush(
                    pq, PQItem(first, nextNode, cost + nextNode.value)
                )

            first.value = cost
            merged[second.left] = True

        return count


nums = [5, 2, 3, 1]
print(Solution().minimumPairRemoval(nums))
nums = [1, 2, 2]
print(Solution().minimumPairRemoval(nums))
