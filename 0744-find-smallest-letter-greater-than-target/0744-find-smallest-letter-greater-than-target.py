# time complexity: O(logn)
# space complexity: O(1)
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if left == len(letters):
            return letters[0]
        return letters[left]


letters = ["c", "f", "j"]
target = "j"
print(Solution().nextGreatestLetter(letters, target))
