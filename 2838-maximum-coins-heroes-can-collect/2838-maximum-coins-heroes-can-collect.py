# time complexity: O((m+n)logm)
# space complexity: O(m+S)
from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:

        monsterCoins = []
        for i in range(len(monsters)):
            monsterCoins.append([monsters[i], coins[i]])
        monsterCoins.sort()
        for i in range(1, len(monsterCoins)):
            monsterCoins[i][1] += monsterCoins[i-1][1]

        result = []
        for i in range(len(heroes)):
            target = heroes[i]
            left = 0
            right = len(monsterCoins) - 1

            while left <= right:
                mid = (left + right) // 2
                if monsterCoins[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if left == 0 and monsterCoins[left][0] > target:
                result.append(0)
            else:
                result.append(monsterCoins[right][1])
        return result


heroes = [4, 4]
monsters = [5, 7, 8]
coins = [1, 1, 1]
print(Solution().maximumCoins(heroes, monsters, coins))
