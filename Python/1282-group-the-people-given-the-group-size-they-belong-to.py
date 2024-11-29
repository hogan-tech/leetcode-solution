from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        szToGroup = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in szToGroup:
                szToGroup[size] = []
            szToGroup[size].append(i)
            if len(szToGroup[size]) == size:
                result.append(szToGroup[size])
                szToGroup[size] = []
        return result


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(Solution().groupThePeople(groupSizes))
