# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
print(Solution().sortPeople(names, heights))
