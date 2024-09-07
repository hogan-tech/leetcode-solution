# time complexity: O(m^n * n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start):
            if len(octets) == 4 and start == len(s):
                ips.append('.'.join(octets))
                return
            for size in range(1, 4):
                octet = s[start:start + size]
                if len(octet) > 1 and (octet[0] == '0' or int(octet) > 255):
                    continue
                if len(octets) < 4:
                    octets.append(octet)
                    backtrack(start + size)
                    octets.pop()
        octets = []
        ips = []
        backtrack(0)
        return ips


s = "25525511135"
print(Solution().restoreIpAddresses(s))
