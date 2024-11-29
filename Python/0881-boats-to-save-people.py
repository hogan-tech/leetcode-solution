# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            ans += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return ans


people = [1, 2]
limit = 3
print(Solution().numRescueBoats(people, limit))
