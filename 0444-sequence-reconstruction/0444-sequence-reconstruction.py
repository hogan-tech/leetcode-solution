# time complexity: O(L + V + E)
# space complexity: O(v + E)
from collections import defaultdict, deque
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        values = {x for sequence in sequences for x in sequence}
        adjList = defaultdict(list)
        indegrees = defaultdict(int)
        for value in values:
            indegrees[value] = 0

        for sequence in sequences:
            for i in range(len(sequence) - 1):
                u = sequence[i]
                v = sequence[i+1]
                adjList[u].append(v)
                indegrees[v] += 1

        queue = deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)

        result = []
        while queue:
            if len(queue) != 1:
                return False
            currNode = queue.popleft()
            result.append(currNode)
            for nextNode in adjList[currNode]:
                indegrees[nextNode] -= 1
                if indegrees[nextNode] == 0:
                    queue.append(nextNode)

        return len(result) == len(values) and result == nums


nums = [1, 2, 3]
sequences = [[1, 2], [1, 3]]
print(Solution().sequenceReconstruction(nums, sequences))
nums = [1, 2, 3]
sequences = [[1, 2]]
print(Solution().sequenceReconstruction(nums, sequences))
nums = [1, 2, 3]
sequences = [[1, 2], [1, 3], [2, 3]]
print(Solution().sequenceReconstruction(nums, sequences))
