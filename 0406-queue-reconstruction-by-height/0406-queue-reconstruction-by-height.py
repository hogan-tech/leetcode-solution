# time complexity: O(n^2 + nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))
people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
print(Solution().reconstructQueue(people))
