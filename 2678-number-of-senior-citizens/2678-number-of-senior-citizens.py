# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1
        return count


details = ["9751302862F0693", "3888560693F7262", "5485983835F0649",
           "2580974299F6042", "9976672161M6561", "0234451011F8013", "4294552179O6482"]
print(Solution().countSeniors(details))
