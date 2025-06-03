# time complexity: O(N + M)
# space complexity: O(N + M)
from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        if not initialBoxes:
            return 0

        ownedBoxes = set(initialBoxes)
        keysOwned = set()
        locked = set()

        queue = deque(initialBoxes)
        opened = set()
        result = 0

        while queue:
            currBox = queue.popleft()

            if currBox in opened:
                continue

            if status[currBox] == 1 or currBox in keysOwned:
                opened.add(currBox)
                result += candies[currBox]

                for key in keys[currBox]:
                    if key not in keysOwned:
                        keysOwned.add(key)
                        if key in locked:
                            locked.remove(key)
                            queue.append(key)

                for newBox in containedBoxes[currBox]:
                    if newBox not in ownedBoxes:
                        ownedBoxes.add(newBox)
                        queue.append(newBox)

            else:
                locked.add(currBox)

        return result


'''
boxs
if status of box is 1, open directily, else need key

0: 1, 2
1: 3

status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
'''
status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))
status = [1, 0, 0, 0, 0, 0]
candies = [1, 1, 1, 1, 1, 1]
keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
initialBoxes = [0]
print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))
