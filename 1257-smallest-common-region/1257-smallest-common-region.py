# time complexity: O(m*n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def fetchPathForRegion(self, currNode: str, childParentMap: set) -> List[str]:
        path = []
        path.append(currNode)
        while currNode in childParentMap:
            parentNode = childParentMap[currNode]
            path.append(parentNode)
            currNode = parentNode

        path.reverse()
        return path

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        childParentMap = {}
        for region in regions:
            parentNode = region[0]
            for i in range(1, len(region)):
                childParentMap[region[i]] = parentNode

        path1 = self.fetchPathForRegion(region1, childParentMap)
        path2 = self.fetchPathForRegion(region2, childParentMap)
        print(path1)
        print(path2)
        i, j = 0, 0
        lowesCommonAncestor = ""
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            lowesCommonAncestor = path1[i]
            i += 1
            j += 1
        return lowesCommonAncestor


regions = [["Earth", "North America", "South America"],
           ["North America", "United States", "Canada"],
           ["United States", "New York", "Boston"],
           ["Canada", "Ontario", "Quebec"],
           ["South America", "Brazil"]]
region1 = "Quebec"
region2 = "New York"
print(Solution().findSmallestRegion(regions, region1, region2))
