# time complexity: O(n*m)
# space complexity: O(n*m)
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileMap = defaultdict(list)
        for path in paths:
            values = path.split(' ')
            for i in range(1, len(values)):
                nameContent = values[i].split('(')
                content = nameContent[1][:-1]
                directory = values[0]
                fileName = nameContent[0]
                filePath = f"{directory}/{fileName}"
                fileMap[content].append(filePath)

        result = []
        for paths in fileMap.values():
            if len(paths) > 1:
                result.append(paths)

        return result


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
         "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(Solution().findDuplicate(paths))
paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
         "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]
print(Solution().findDuplicate(paths))
