# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def maxUpgrades(self, countList: List[int], upgradeList: List[int], sellList: List[int], moneyList: List[int]) -> List[int]:
        resultList = []
        n = len(countList)
        for i in range(n):
            count = countList[i]
            upgrade = upgradeList[i]
            sell = sellList[i]
            money = moneyList[i]
            resultList.append(min(count, int(
                (money + count * sell) / (upgrade + sell))))
        return resultList


count = [4, 3]
upgrade = [3, 5]
sell = [4, 2]
money = [8, 9]
print(Solution().maxUpgrades(count, upgrade, sell, money))
