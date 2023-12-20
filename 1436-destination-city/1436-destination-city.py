# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hasBeen = set()
        for i in range(len(paths)):
            hasBeen.add(paths[i][0])

        for i in range(len(paths)):
            if (paths[i][1] not in hasBeen):
                return paths[i][1]
        return ""


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(Solution().destCity(paths))
