# time complexity: O(b)
# space complexity: O(1)
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        seen = {startGene}
        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor in bank and neighbor not in seen:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)
        return -1


startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(Solution().minMutation(startGene, endGene, bank))
