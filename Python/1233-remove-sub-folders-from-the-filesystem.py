# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            lastFolder = result[-1]
            lastFolder += "/"

            if not folder[i].startswith(lastFolder):
                result.append(folder[i])

        return result


folders = ["/a", "/a/b/c", "/a/b/d"]
print(Solution().removeSubfolders(folders))
