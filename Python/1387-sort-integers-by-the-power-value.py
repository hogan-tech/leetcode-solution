# time complexity: O(nlogm + nlogn)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powerHashSet = defaultdict(int)

        def getPowerValue(num):
            count = 0
            while num != 1:
                if num in powerHashSet:
                    return powerHashSet[num]
                if num % 2:
                    num = 3 * num + 1
                else:
                    num //= 2
                count += 1

            powerHashSet[num] = count
            return count

        orderList = []
        for num in range(lo, hi + 1):
            orderList.append([getPowerValue(num), num])
        orderList.sort()
        return orderList[k - 1][1]


lo = 12
hi = 15
k = 2
print(Solution().getKth(lo, hi, k))
lo = 7
hi = 11
k = 4
print(Solution().getKth(lo, hi, k))
