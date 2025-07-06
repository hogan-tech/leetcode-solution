# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List
import re


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validBusiness = ["electronics", "grocery", "pharmacy", "restaurant"]
        result = []
        coupons = []
        order = {business: i for i, business in enumerate(validBusiness)}
        for currCode, currBusiness, currActive in zip(code, businessLine, isActive):
            if currActive and currBusiness in validBusiness and re.fullmatch(r'[A-Za-z0-9_]+', currCode):
                coupons.append((order[currBusiness], currBusiness, currCode))
        coupons.sort()
        result = [coupon[2] for coupon in coupons]
        return result


code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
isActive = [True, True, True, True]
print(Solution().validateCoupons(code, businessLine, isActive))
code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"]
businessLine = ["grocery", "electronics", "invalid"]
isActive = [False, True, True]
print(Solution().validateCoupons(code, businessLine, isActive))
