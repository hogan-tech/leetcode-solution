# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBillCount = 0
        tenBillCount = 0
        for bill in bills:
            if bill == 5:
                fiveBillCount += 1
            elif bill == 10:
                if fiveBillCount == 0:
                    return False
                else:
                    fiveBillCount -= 1
                    tenBillCount += 1
            else:
                if fiveBillCount > 0 and tenBillCount > 0:
                    fiveBillCount -= 1
                    tenBillCount -= 1
                elif fiveBillCount >= 3:
                    fiveBillCount -= 3
                else:
                    return False
        return True


bills = [5, 5, 10, 10, 20]
print(Solution().lemonadeChange(bills))
