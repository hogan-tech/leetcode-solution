# time complexity: O(n*w)
# space complexity: O(n*w)
from functools import cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def place(bookPos, curWidth, maxHeight):
            if bookPos == len(books):
                return 0
            width, height = books[bookPos]
            ans = height + place(bookPos + 1, width, height)
            if bookPos and curWidth + width <= shelfWidth:
                heightIncrease = max(0, height - maxHeight)
                ans = min(ans, heightIncrease + place(bookPos + 1,
                                                      curWidth + width, maxHeight + heightIncrease))

            return ans

        return place(0, 0, 0)


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelfWidth = 4
print(Solution().minHeightShelves(books, shelfWidth))
