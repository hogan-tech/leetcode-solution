# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupDict = defaultdict(list)
        for i in range(len(groupSizes)):
            currGroup = groupSizes[i]
            groupDict[currGroup].append(i)

        result = []
        for key, groupList in groupDict.items():
            if len(groupList) == key:
                result.append(groupList)
            else:
                while len(groupList) > key:
                    result.append(groupList[:key])
                    groupList = groupList[key:]
                result.append(groupList)

        return result


groupSizes = [3, 3, 3, 3, 3, 1, 3]
print(Solution().groupThePeople(groupSizes))
groupSizes = [2, 1, 3, 3, 3, 2]
print(Solution().groupThePeople(groupSizes))
