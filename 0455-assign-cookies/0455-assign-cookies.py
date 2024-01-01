from typing import List


class Solution:
	def findContentChildren(self, greedyChildren: List[int], cookiesSize: List[int]) -> int:
		greedyChildren.sort()
		cookiesSize.sort()
		cookieIdx = 0
		childrenIdx = 0
		while cookieIdx < len(cookiesSize) and childrenIdx < len(greedyChildren):
			if cookiesSize[cookieIdx] >= greedyChildren[childrenIdx]:
				childrenIdx += 1
			cookieIdx += 1
		return childrenIdx


greedyChildren = [1, 2, 3]
cookiesSize = [1, 1]
print(Solution().findContentChildren(greedyChildren, cookiesSize))
