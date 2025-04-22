# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        playerScore = [0] * len(skills)
        player = [i for i in range(len(skills))]

        if k > len(skills):
            return skills.index(max(skills))

        while playerScore[player[0]] < k:
            firstPlayer = player[0]
            secondPlayer = player[1]
            if skills[firstPlayer] > skills[secondPlayer]:
                player.pop(1)
                player.append(secondPlayer)
                playerScore[firstPlayer] += 1
            else:
                player.pop(0)
                player.append(firstPlayer)
                playerScore[secondPlayer] += 1

        return player[0]


skills = [4, 2, 6, 3, 9]
k = 2
print(Solution().findWinningPlayer(skills, k))
skills = [2, 5, 4]
k = 3
print(Solution().findWinningPlayer(skills, k))
skills = [16, 4, 7, 17]
k = 562084119
print(Solution().findWinningPlayer(skills, k))
