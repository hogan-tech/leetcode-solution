# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:

        from collections import defaultdict
        graph = defaultdict(int)
        for num in nums:
            depth, pos, val = num//100, (num//10) % 10, num % 10
            graph[depth, pos] = val

        stack = []

        curDepth, curPos = 1, 1
        curPathSum = graph[curDepth, curPos]
        stack.append((curPathSum, (curDepth, curPos)))
        returnedAllPathsSum = 0

        while stack:

            curPathSum, (curDepth, curPos) = stack.pop()

            leftDepth = rightDepth = 1 + curDepth
            leftPos, rightPos = 2*curPos-1, 2*curPos

            if (leftDepth, leftPos) not in graph and (rightDepth, rightPos) not in graph:
                returnedAllPathsSum += curPathSum
            else:
                if (leftDepth, leftPos) in graph:
                    leftPathSum = curPathSum + graph[leftDepth, leftPos]
                    stack.append((leftPathSum, (leftDepth, leftPos)))
                if (rightDepth, rightPos) in graph:
                    rightPathSum = curPathSum + graph[rightDepth, rightPos]
                    stack.append((rightPathSum, (rightDepth, rightPos)))

        return returnedAllPathsSum


nums = [113, 215, 221]
print(Solution().pathSum(nums))
